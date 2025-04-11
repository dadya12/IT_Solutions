from django import forms
from webapp.models.type_status import Status, TransactionType
from webapp.models.categories import Category, SubCategory

class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = '__all__'


class SubCategoryForm(forms.ModelForm):
  class Meta:
    model = SubCategory
    fields = '__all__'


class StatusForm(forms.ModelForm):
  class Meta:
    model = Status
    fields = '__all__'


class TransactionTypeForm(forms.ModelForm):
  class Meta:
    model = TransactionType
    fields = '__all__'