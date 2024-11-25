from django import forms
from .models import Transaction, Account, ModelMapping, AccountMapping

class TransactionForm(forms.ModelForm):
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