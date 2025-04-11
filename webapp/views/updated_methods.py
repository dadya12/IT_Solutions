from django.urls import reverse_lazy
from django.views.generic import UpdateView
from webapp.models.categories import Category, SubCategory
from webapp.models.type_status import Status, TransactionType
from webapp.forms.update_forms import CategoryUpdateForm, SubCategoryUpdateForm, StatusUpdateForm, TransactionTypeUpdateForm


class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryUpdateForm
    template_name = 'update_templates/category_update.html'
    success_url = reverse_lazy('webapp:control')


class SubCategoryUpdate(UpdateView):
    model = SubCategory
    form_class = SubCategoryUpdateForm
    template_name = 'update_templates/subcategory_update.html'
    success_url = reverse_lazy('webapp:control')


class StatusUpdate(UpdateView):
    model = Status
    form_class = StatusUpdateForm
    template_name = 'update_templates/status_update.html'
    success_url = reverse_lazy('webapp:control')


class TransactionTypeUpdate(UpdateView):
    model = TransactionType
    form_class = TransactionTypeUpdateForm
    template_name = 'update_templates/transaction_type_update.html'
    success_url = reverse_lazy('webapp:control')
