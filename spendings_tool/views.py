from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
from .models import Transaction, Account
from .forms import TransactionForm
from django.contrib import messages
from django.core.files.storage import default_storage

def home(request):
    return render(request, "home.html")

def import_data(request):
    context = {}
    if request.method == "GET":
        return render(request, "upload_csv.html")
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
        context["headers"] = headers
        fields = [f.name for f in Transaction._meta.get_fields()]
        fields.append("amount_negative")
        context["fields"] = fields

        return render(request, "import_data.html", context)

def process_data(request, file_name):
    file_data = default_storage.open("files/" + file_name + ".csv").read().decode("utf-8")
    lines = file_data.split("\n")
    post = request.POST
    postArr = [post.get("id"),
               post.get("account"),
               post.get("name"),
               post.get("date"),
               post.get("amount"),
               post.get("category"),
               post.get("amount_negative")]
    lines.pop(0)
    arr = []
    for line in lines:
        if line != '':
            fields = line.split(",")
            data = {}
            if postArr[0] != "S" : data["id"] = fields[int(postArr[0])]
            if postArr[1] != "S" : data["account"] = Account.objects.get(account_number=fields[int(postArr[1])])
            if postArr[2] != "S" : data["name"] = fields[int(postArr[2])]
            if postArr[3] != "S" : data["date"] = fields[int(postArr[3])]
            if postArr[4] != "S" : 
                if postArr[6] == "S" : data["amount"] = fields[int(postArr[4])]
                else : 
                    a = fields[int(postArr[4])]
                    a_neg = fields[int(postArr[6])]
                    if a != "" : data["amount"] = a
                    else : data["amount"] = -float(a_neg)
            if postArr[5] != "S" : data["category"] = fields[int(postArr[5])]
            
            try:
                form = TransactionForm(data)
                if form.is_valid():
                    form.save()
                else:
                    messages.error(request, form.errors.as_json())
            except Exception as e:
                messages.error(request, repr(e))
    return redirect(reverse("import_data"))

def transaction_list(request):
    context = {}

    search = request.GET.get("search", "")
    after = request.GET.get("after", "0001-01-01")
    before = request.GET.get("before", "3000-01-01")
    if after == "": after = "0001-01-01"
    if before == "": before = "3000-01-01"
    
    context["transactions"] = Transaction.objects.filter(name__contains=search).filter(date__gte=after).filter(date__lte=before)

    return render(request, "transactions_list_view.html", context)

def show_transaction(request, id):
    context = {}

    context["transaction"] = Transaction.objects.get(id=id)

    return render(request, "view_transaction.html", context)

def update_transaction(request, id):
    context = {}

    transaction = get_object_or_404(Transaction, id=id)

    form = TransactionForm(request.POST or None, instance=transaction)

    if form.is_valid():
        form.save()
        return redirect(show_transaction, id=id)
    
    context["form"] = form

    return render(request, "update.html", context)

def accounts_list(request):
    context = {}
    
    context["accounts"] = Account.objects.all()

    return render(request, "accounts_list_view.html", context)

def show_account(request, id):
    context = {}

    context["account"] = Account.objects.get(id=id)

    return render(request, "view_account.html", context)
    