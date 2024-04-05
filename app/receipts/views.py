from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ReceiptsForm
from .models import Receipts


class ReceiptsListView(ListView):
    model = Receipts

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Receipts.objects.filter(
                Q(electrical__name__icontains=query)
                | Q(amount__icontains=query)
                | Q(receipt_no__icontains=query)
                | Q(notes__icontains=query)
            ).distinct()
        return super().get_queryset()


class ReceiptsDetailView(DetailView):
    model = Receipts


class ReceiptsCreateView(CreateView):
    model = Receipts
    form_class = ReceiptsForm


class ReceiptsUpdateView(UpdateView):
    model = Receipts
    form_class = ReceiptsForm
