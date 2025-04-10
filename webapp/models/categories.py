from django.db import models
from webapp.models.type_status import TransactionType


class Category(models.Model):
    name = models.CharField(max_length=100)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE, related_name='categories', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return f"{self.name} ({self.category.name})"