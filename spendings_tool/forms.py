from django import forms
from .models import Transaction, Account, ModelMapping, Category

class TransactionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y']
    )

    account = forms.ModelChoiceField(widget=forms.Select(), empty_label=None, queryset=Account.objects.all())

    class Meta:
        model = Transaction

        fields = [
            "name",
            "amount",
            "account",
            "balance",
            "date",
        ]

class AccountForm(forms.ModelForm):

    class Meta:
        model = Account

        fields = [
            "name",
            "account_number",
            "account_type",
            "currency",
        ]

class ModelMappingForm(forms.ModelForm):
    class Meta:
        model = ModelMapping

        fields = [
            "name",
            "field"
        ]
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

        fields = [
            "name"
        ]