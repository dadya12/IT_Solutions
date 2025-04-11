from django.views.generic import CreateView
from django.urls import reverse_lazy
from webapp.models.type_status import Status, TransactionType
from webapp.models.categories import Category, SubCategory
from webapp.forms.create_forms import CategoryForm, SubCategoryForm, StatusForm, TransactionTypeForm


class CategoryCreate(CreateView):
  template_name = 'create_templates/category_create.html'
  model = Category
  success_url = reverse_lazy('webapp:control')
  form_class = CategoryForm



class SubCategoryCreate(CreateView):
  template_name = 'create_templates/subcategory_create.html'
  model = SubCategory
  success_url = reverse_lazy('webapp:control')
  form_class = SubCategoryForm



class StatusCreate(CreateView):
  template_name = 'create_templates/status_create.html'
  model = Status
  success_url = reverse_lazy('webapp:control')
  form_class = StatusForm



class TransactionTypeCreate(CreateView):
  template_name = 'create_templates/transaction_type_create.html'
  model = TransactionType
  success_url = reverse_lazy('webapp:control')
  form_class = TransactionTypeForm