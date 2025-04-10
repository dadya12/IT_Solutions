from django.shortcuts import render
from django.views.generic import ListView
from webapp.models.categories import Category, SubCategory
from webapp.models.transaction import Transaction
from webapp.models.type_status import Status, TransactionType


class TransactionList(ListView):
  template_name = 'home_page.html'
  context_object_name = 'transactions'
  model = Transaction

  def get_queryset(self):
    queryset = Transaction.objects.all()
    pass