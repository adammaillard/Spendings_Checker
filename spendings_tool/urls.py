from django.urls import path
from . import views

urlpatterns = [
    path('transactions/<int:id>/edit/', views.update_transaction, name='update_transaction'),
    path('transactions/create/', views.create_transaction, name='create_transaction'),
    path('transactions/<int:id>/', views.show_transaction, name='show_transaction'),
    path('import/<slug:file_name>/', views.process_data, name ='process_data'),
    path('import/', views.import_data, name ='import_data'),
    path('accounts/create/', views.create_account, name='create_account'),
    path('accounts/<int:id>', views.show_account, name='show_account'),
    path('accounts/', views.accounts_list, name='account_list'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('mappings/add_account/<slug:account_number>/', views.add_account_mapping, name="add_account_mapping"),
    path('mappings/edit/<int:id>', views.model_mappings_edit, name='edit_mapping'),
    path('mappings/', views.model_mappings_list, name='mappings_list'),
    path('', views.home, name="home")
]
