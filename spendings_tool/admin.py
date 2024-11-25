from django.contrib import admin
from .models import Account, Transaction, Category, AccountMapping

# Register your models here.
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(AccountMapping)