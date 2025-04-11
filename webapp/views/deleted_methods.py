from django.urls import reverse_lazy
from django.views.generic import DeleteView
from webapp.models.categories import Category, SubCategory
from webapp.models.type_status import Status, TransactionType


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('webapp:control')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class SubCategoryDelete(DeleteView):
    model = SubCategory
    success_url = reverse_lazy('webapp:control')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class StatusDelete(DeleteView):
    model = Status
    success_url = reverse_lazy('webapp:control')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class TransactionTypeDelete(DeleteView):
    model = TransactionType
    success_url = reverse_lazy('webapp:control')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
