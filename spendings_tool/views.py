from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
from .models import Transaction, Account, Category, ModelMapping, AccountMapping
from .forms import TransactionForm, AccountForm, ModelMappingForm
from django.contrib import messages
from django.core.files.storage import default_storage

def home(request):
    context = {}

    accounts = Account.objects.all()
    accounts_list = []
    
    total_balance = 0
    for account in accounts:
        account_dict = {}
        account_dict["name"] = account.name
        transactions = Transaction.objects.filter(account=account.id).order_by("-date")
        account_dict["balance"] = transactions[0].balance
        account_dict["spendings"] = 0
        for transaction in transactions:
            account_dict["spendings"] += transaction.amount
        total_balance += account_dict["balance"]
        account_dict["balance"] = account.currency + str(account_dict["balance"])
        account_dict["number"] = account.account_number
        account_dict["id"] = account.id
        accounts_list.append(account_dict)

    
    context["accounts"] = accounts_list
    context["total_balance"] = "£" + str(total_balance)

    return render(request, "home.html", context)

#Allows user to import transactions using csv files
def import_data(request):
    context = {}

    # Allow user to post csv file if request is GET
    if request.method == "GET":
        return render(request, "upload_csv.html")
    
    # If user POSTs a csv file break down the file into headers and send user import_data.html to allow them to pick 
    # which collums of the csv are what transaction attributes
    if request.method == "POST":

        csv_file = request.FILES["csv_file"]

        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return redirect(reverse("import_data"))
        
        default_storage.delete("files/" + csv_file.name)
        default_storage.save("files/" + csv_file.name, csv_file)
        context["file_name"] = csv_file.name.removesuffix('.csv')

        file_data = default_storage.open("files/" + csv_file.name).read().decode("utf-8")
        lines = file_data.split("\n")
        headers = lines[0].split(",")

        to_map = []

        for header in headers:
            header = header.strip()
            header_lower = header.lower()
            try:
                ModelMapping.objects.get(name=header_lower)
            except ModelMapping.DoesNotExist:
                to_map.append(header)

        if len(to_map) == 0:
            return redirect(process_data, context["file_name"])

        context["to_map"] = to_map

        return render(request, "import_data.html", context)

def add_mappings(request):
    post = request.POST
    for header in post:
        if header != "csrfmiddlewaretoken":
            ModelMapping.objects.create(name=header.lower(),field=post.get(header))

def check_mappings(file_name):
    file_data = default_storage.open("files/" + file_name + ".csv").read().decode("utf-8")
    lines = file_data.split("\n")
    headers = lines[0].split(",")
    headers_striped = [header.strip() for header in headers]

    dict = {
        "account": None,
        "name": None,
        "date": None,
        "amount": None,
        "balance": None 
    }

    for index,header in enumerate(headers_striped):
        mapping = ModelMapping.objects.get(name=header.lower())
        if mapping.field != "skip":
            dict[mapping.field] = index
    
    return dict

def get_account_mapping(account_number):
    try:
        return AccountMapping.objects.get(account_number=account_number).account
    except AccountMapping.DoesNotExist:
        return None

def add_account_mapping(request, account_number):
    if request.method == 'GET':
        context = {"account_number":account_number}
        context["accounts"] = Account.objects.all()
        return render(request, "add_mapping.html", context)
    if request.method == 'POST':
        account = Account.objects.get(id=request.POST.get("account"))
        AccountMapping.objects.create(account_number=account_number,account=account)
        return redirect(import_data)

# Follow up method to import_data()
# When the user inputs which collum is what field try to create transactions using the csv file
def process_data(request, file_name):
    add_mappings(request)
    mappings = check_mappings(file_name)

    if None in mappings.values():
        output = "Missing Mappings for:"
        for mapping in mappings.keys():
            if mappings[mapping] == None:
                output += mapping + ", "
        messages.info(request,output)
        return redirect(reverse("mappings_list"))
    
    file_data = default_storage.open("files/" + file_name + ".csv").read().decode("utf-8")
    lines = file_data.split("\n")
    lines.pop(0)
   
    for line in lines:
        if line != '':
            fields = line.split(",")
            data = {}
            data["account"] = fields[mappings["account"]]
            data["name"] = fields[mappings["name"]]
            data["date"] = fields[mappings["date"]]
            data["amount"] = fields[mappings["amount"]]
            data["balance"] = fields[mappings["balance"]]

            account = get_account_mapping(data["account"])
            if account == None:
                return redirect(add_account_mapping, data["account"])
            data["account"] = account
            data["amount"] = 0

            form = TransactionForm(data)
            if form.is_valid():
                form.save()
            else:
                output = ""
                for field in form:
                    output += field.errors
                return HttpResponse(output)
    return redirect(reverse("import_data"))

def model_mappings_list(request):
    context = {}

    context["mappings"] = ModelMapping.objects.all()

    return render(request, "mappings_list_view.html", context)

def model_mappings_edit(request,id):

    context = {}

    mapping = get_object_or_404(ModelMapping, id=id)

    form = ModelMappingForm(request.POST or None, instance=mapping)

    if form.is_valid():
        form.save()
        return redirect("mappings_list")
    
    context["form"] = form

    return render(request, "update.html", context)

# Returns a list of all transactions
# Allows for filtering of transactions using search and dates
def transaction_list(request):

    context = {}
    
    def get_category(obj):
        if obj.category == None:
            return "-"
        else:
            return Category.objects.get(id=obj.category)

    transactions = Transaction.objects.all().order_by('-date')
    context["transactions"] = zip(map(get_category, transactions),transactions)

    return render(request, "transactions_list_view.html", context)

# Returns a single transaction
def show_transaction(request, id):

    context = {}

    context["transaction"] = Transaction.objects.get(id=id)

    return render(request, "view_transaction.html", context)

# Allows the user to update a transaction
def update_transaction(request, id):

    context = {}

    transaction = get_object_or_404(Transaction, id=id)

    form = TransactionForm(request.POST or None, instance=transaction)

    if form.is_valid():
        form.save()
        return redirect(show_transaction, id=id)
    
    context["form"] = form

    return render(request, "update.html", context)

def create_transaction(request):
    context = {}
    form = TransactionForm(request.POST or None)

    if form.is_valid():
        transaction = form.save()
        return redirect(show_transaction, id=transaction.id )
    
    context["form"] = form

    return render(request, "update.html", context)

# Returns a list of all accounts
def accounts_list(request):

    context = {}
    
    accounts = Account.objects.all()

    context["accounts"] = []

    for account in accounts:
        account_dict = {}
        account_dict["name"] = account.name
        account_dict["id"] = account.id
        account_dict["number"] = account.account_number
        transactions = Transaction.objects.filter(account=account.id).order_by("-date")
        account_dict["balance"] = transactions[0].balance
        account_dict["spendings"] = 0
        for transaction in transactions:
            account_dict["spendings"] += transaction.amount
        account_dict["balance"] = account.currency + str(account_dict["balance"])
        context["accounts"].append(account_dict)

    return render(request, "accounts_list_view.html", context)

# Returns an account from an id
def show_account(request, id):

    context = {}

    context["account"] = Account.objects.get(id=id)

    return render(request, "view_account.html", context)

def create_account(request):
    context = {}
    form = AccountForm(request.POST or None)

    if form.is_valid():
        account = form.save()
        return redirect(show_account, id=account.id )
    
    context["form"] = form

    return render(request, "update.html", context)
    