from django.db.models import Q
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import WiremanForm
from .models import Category, Wireman


class WiremanListView(ListView):
    model = Wireman

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Wireman.objects.filter(
                Q(name__icontains=query)
                | Q(license_no__icontains=query)
                | Q(category__name__icontains=query)
                | Q(address__icontains=query)
                | Q(email__icontains=query)
                | Q(phone__icontains=query)
                | Q(notes__icontains=query)
            ).distinct()
        return super().get_queryset()


class WiremanDetailView(DetailView):
    model = Wireman


class WiremanCreateView(CreateView):
    model = Wireman
    form_class = WiremanForm


class WiremanUpdateView(UpdateView):
    model = Wireman
    form_class = WiremanForm
