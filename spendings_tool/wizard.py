import data_wizard
from .models import Account,Transaction,Category

data_wizard.register(Account)
data_wizard.register(Transaction)
data_wizard.register(Category)