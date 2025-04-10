from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from webapp.models.categories import Category, SubCategory
from webapp.models.transaction import Transaction
from webapp.models.type_status import Status, TransactionType
from webapp.forms.transaction_forms import TransactionForm



class TransactionList(ListView):
  template_name = 'home_page.html'
  context_object_name = 'transactions'
  model = Transaction

  def get_queryset(self):
    queryset = Transaction.objects.all()
    date_from = self.request.GET.get('date_from')
    date_to = self.request.GET.get('date_to')
    if date_from and date_to:
      queryset = queryset.filter(created_at__range=[date_from, date_to])
    elif date_from:
      queryset = queryset.filter(created_at__gte=date_from)
    elif date_to:
      queryset = queryset.filter(created_at__lte=date_to)
    
    status = self.request.GET.get('status')
    if status:
      queryset = queryset.filter(status__id=int(status))
    
    transaction_type = self.request.GET.get('transaction_type')
    if transaction_type:
      queryset = queryset.filter(transaction_type__id=int(transaction_type))

    category = self.request.GET.get('category')
    if category:
      queryset = queryset.filter(category__id=int(category))


    subcategory = self.request.GET.get('subcategory')
    if subcategory:
      queryset = queryset.filter(subcategory__id=int(subcategory))

    return queryset
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['categories'] = Category.objects.all()
    context['subcategories'] = SubCategory.objects.all()
    context['statuses'] = Status.objects.all()
    context['transaction_types'] = TransactionType.objects.all()
    return context
  

class TransactionCreate(CreateView):
  template_name = 'transactions/transaction_create.html'
  model = Transaction
  success_url = reverse_lazy('webapp:home')
  form_class = TransactionForm