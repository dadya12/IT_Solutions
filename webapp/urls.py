from django.urls import path
from webapp.views.transaction import TransactionList, TransactionCreate

app_name = 'webapp'

urlpatterns = [
  path('', TransactionList.as_view(), name='home'),
  path('create/transaction', TransactionCreate.as_view(), name='create_transaction'),
]