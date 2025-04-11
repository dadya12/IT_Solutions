from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from webapp.models.type_status import TransactionType, Status
from webapp.models.categories import Category, SubCategory


class Transaction(models.Model):
  created_at = models.DateField(default=timezone.now, verbose_name='Дата создания записи')
  status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
  transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE, verbose_name='Тип')
  category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
  subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
  price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Сумма')
  comment = models.TextField(max_length=500, verbose_name='Комментарий', null=True, blank=True)

  def __str__(self):
        return f"{self.created_at} — {self.transaction_type.name} — {self.price}₽"