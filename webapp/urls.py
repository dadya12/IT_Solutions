from django.urls import path
from webapp.views.transaction import TransactionList, TransactionCreate, TransactionUpdate, TransactionDelete, ControlListView
from webapp.views.creation_methods import CategoryCreate, SubCategoryCreate, StatusCreate, TransactionTypeCreate
from webapp.views.updated_methods import CategoryUpdate, SubCategoryUpdate, StatusUpdate, TransactionTypeUpdate
from webapp.views.deleted_methods import CategoryDelete, SubCategoryDelete, StatusDelete, TransactionTypeDelete


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

  path('update/category/<int:pk>', CategoryUpdate.as_view(), name='category_update'),
  path('update/subcategory/<int:pk>', SubCategoryUpdate.as_view(), name='subcategory_update'),
  path('update/status/<int:pk>', StatusUpdate.as_view(), name='status_update'),
  path('update/transaction_type/<int:pk>', TransactionTypeUpdate.as_view(), name='transaction_type_update'),

  path('delete/category/<int:pk>', CategoryDelete.as_view(), name='category_delete'),
  path('delete/subcategory/<int:pk>', SubCategoryDelete.as_view(), name='subcategory_delete'),
  path('delete/status/<int:pk>', StatusDelete.as_view(), name='status_delete'),
  path('delete/transaction_type/<int:pk>', TransactionTypeDelete.as_view(), name='transaction_type_delete'),

  path('control', ControlListView.as_view(), name='control'),

]