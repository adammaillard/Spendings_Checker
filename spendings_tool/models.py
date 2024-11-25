from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=32)
    account_number = models.IntegerField()
    account_type = models.CharField(choices={"CA":"Current","SA":"Savings","ISA":"ISA"},max_length=7)
    currency = models.CharField(choices={"£":"Pound","€":"Euro"},max_length=5)
    
class Transaction(models.Model):
    account = models.ForeignKey("Account", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=64)
    date = models.DateField()
    amount = models.DecimalField(decimal_places=2,max_digits=10,default=0)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, default=None)
    balance = models.DecimalField(decimal_places=2,max_digits=10,default=0)

class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)

class ModelMapping(models.Model):
    name = models.CharField(max_length=64)
    field = models.CharField(choices={
        "account":"Account Number","name":"Transaction Description","date":"Transaction Date","amount":"Transaction Amount","balance":"Account Balance","skip":"Skip"
    },max_length=7)

class AccountMapping(models.Model):
    account_number = models.IntegerField()
    account = models.ForeignKey("Account", on_delete=models.DO_NOTHING)