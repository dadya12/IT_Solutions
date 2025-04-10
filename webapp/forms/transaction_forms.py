from django import forms
from webapp.models.transaction import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['status', 'transaction_type', 'category', 'subcategory', 'price', 'comment']