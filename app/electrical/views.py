from django.db.models import Q
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ElectricalForm
from .models import Category, Electrical


class ElectricalListView(ListView):
    model = Electrical

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Electrical.objects.filter(
                Q(name__icontains=query)
                | Q(license_no__icontains=query)
                | Q(category__name__icontains=query)
                | Q(address__icontains=query)
                | Q(email__icontains=query)
                | Q(phone__icontains=query)
                | Q(notes__icontains=query)
            ).distinct()
        return super().get_queryset()


class ElectricalDetailView(DetailView):
    model = Electrical


class ElectricalCreateView(CreateView):
    model = Electrical
    form_class = ElectricalForm


class ElectricalUpdateView(UpdateView):
    model = Electrical
    form_class = ElectricalForm
