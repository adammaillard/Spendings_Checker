from django.urls import path
from . import views

urlpatterns = [

    path('transactions/<int:id>/delete/', views.delete_transaction, name='delete_transaction'),
    path('transactions/<int:id>/edit-category/', views.edit_transaction_category, name='edit_transaction_category'),
    path('transactions/<int:id>/edit/', views.update_transaction, name='update_transaction'),
    path('transactions/create/', views.create_transaction, name='create_transaction'),
    path('transactions/<int:id>/', views.show_transaction, name='show_transaction'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    
    path('import/<slug:file_name>/', views.process_data, name ='process_data'),
    path('import/', views.import_data, name ='import_data'),
    
    path('accounts/create/', views.create_account, name='create_account'),
    path('accounts/<int:id>/edit', views.update_account, name='update_account'),
    path('accounts/<int:id>', views.show_account, name='show_account'),
    path('accounts/', views.accounts_list, name='account_list'),
    
    path('mappings/add_account/<int:account_number>/', views.add_account_mapping, name="add_account_mapping"),
    path('mappings/edit/<int:id>', views.model_mappings_edit, name='edit_mapping'),
    path('mappings/', views.model_mappings_list, name='mappings_list'),
    
    path('categories/<int:id>/edit', views.edit_category, name='edit_category'),
    path('categories/create', views.create_category, name='create_category'),
    path('categories/', views.show_categories, name='show_categories'),
    
    path('', views.home, name="home")
]
