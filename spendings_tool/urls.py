from django.urls import path
from . import views

urlpatterns = [
    path('transactions/<int:id>/edit/', views.update_transaction, name='update_transaction'),
    path('transactions/<int:id>/', views.show_transaction, name='show_transaction'),
    path('import/<slug:file_name>/', views.process_data, name ='process_data'),
    path('import/', views.import_data, name ='import_data'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('', views.home, name="home")
]
