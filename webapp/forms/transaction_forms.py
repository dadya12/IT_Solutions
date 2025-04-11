from django import forms
from webapp.models.transaction import Transaction
from webapp.models.categories import SubCategory


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['status', 'transaction_type', 'category', 'subcategory', 'price', 'comment']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'transaction_type': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        category = self.initial.get('category')
        if category:
            self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category)
        else:
            self.fields['subcategory'].queryset = SubCategory.objects.none()


    def clean(self):
        cleaned_data = super().clean()
        transaction_type = cleaned_data.get('transaction_type')
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')

        if category and category.transaction_type != transaction_type:
            self.add_error('category', 'Категория не относится к выбранному типу транзакции.')

        if subcategory and subcategory.category != category:
            self.add_error('subcategory', 'Подкатегория не относится к выбранной категории.')