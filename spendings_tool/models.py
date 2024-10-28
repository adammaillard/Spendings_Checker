from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=32)
    account_number = models.IntegerField()
    balance = models.DecimalField(decimal_places=2,max_digits=10)
    account_type = models.CharField(choices={"CA":"Current","SA":"Savings","ISA":"ISA"},max_length=7)
    currency = models.CharField(choices={"£":"Pound","€":"Euro"},max_length=5)
    
class Transaction(models.Model):
    account = models.ForeignKey("Account", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=64)
    date = models.DateField()
    amount = models.DecimalField(decimal_places=2,max_digits=10)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)