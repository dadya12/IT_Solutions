from django.urls import path
from webapp.views.main import TransactionList

app_name = 'webapp'

urlpatterns = [
  path('', TransactionList.as_view(), name='home'),
]