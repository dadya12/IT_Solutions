from django import forms
from webapp.models.transaction import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['status', 'transaction_type', 'category', 'subcategory', 'price', 'comment', 'created_at']


    def clean(self):
        cleaned_data = super().clean()
        transaction_type = cleaned_data.get('transaction_type')
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')

        if category and category.transaction_type != transaction_type:
            self.add_error('category', 'Категория не относится к выбранному типу транзакции.')

        if subcategory and subcategory.category != category:
            self.add_error('subcategory', 'Подкатегория не относится к выбранной категории.')