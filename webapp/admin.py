from django.contrib import admin
from webapp.models.categories import Category, SubCategory
from webapp.models.transaction import Transaction
from webapp.models.type_status import Status, TransactionType


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Transaction)
admin.site.register(Status)
admin.site.register(TransactionType)

    
