from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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

  def get_form_kwargs(self):
     kwargs = super().get_form_kwargs()
     category_id = self.request.GET.get('category')
     if category_id:
        kwargs['initial']['category'] = category_id
     return kwargs
  
  def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     context['selected_category'] = self.request.GET.get('category')
     return context


class TransactionUpdate(UpdateView):
  template_name = 'transactions/transaction_update.html'
  model = Transaction
  form_class = TransactionForm
  success_url = reverse_lazy('webapp:home')


class TransactionDelete(DeleteView):
    model = Transaction
    success_url = reverse_lazy('webapp:home')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


class ControlListView(TemplateView):
    template_name = 'control_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['control_data'] = [
            ('Статусы', Status.objects.all(), 'webapp:status_update', 'webapp:status_delete',
            'webapp:status_create'),
            ('Типы транзакций', TransactionType.objects.all(), 'webapp:transaction_type_update', 'webapp:transaction_type_delete', 'webapp:transaction_type_create'),
            ('Категории', Category.objects.all(), 'webapp:category_update', 'webapp:category_delete', 'webapp:category_create'),
            ('Подкатегории', SubCategory.objects.all(), 'webapp:subcategory_update', 'webapp:subcategory_delete', 'webapp:subcategory_create'),
        ]
        return context