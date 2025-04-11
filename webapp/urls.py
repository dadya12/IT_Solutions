from django.urls import path
from webapp.views.transaction import TransactionList, TransactionCreate, TransactionUpdate, TransactionDelete
from webapp.views.creation_methods import CategoryCreate, SubCategoryCreate, StatusCreate, TransactionTypeCreate

app_name = 'webapp'

urlpatterns = [
  path('', TransactionList.as_view(), name='home'),
  path('create/transaction', TransactionCreate.as_view(), name='create_transaction'),
  path('update/transaction/<int:pk>', TransactionUpdate.as_view(), name='update_transaction'),
  path('delete/transaction/<int:pk>', TransactionDelete.as_view(), name='delete_transaction'),
  path('create/category', CategoryCreate.as_view(), name='category_create'),
  path('create/subcategory', SubCategoryCreate.as_view(), name='subcategory_create'),
  path('create/status', StatusCreate.as_view(), name='status_create'),
  path('create/transaction_type', TransactionTypeCreate.as_view(), name='transaction_type_create'),
]