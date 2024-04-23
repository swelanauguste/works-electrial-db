from django.db.models import Q
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import InspectionForm
from .models import Inspection


class InspectionListView(ListView):
    model = Inspection
    ordering = ["-date"]

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Inspection.objects.filter(
                Q(sheet_no__icontains=query)
                | Q(app_no__icontains=query)
                | Q(inspector__name__icontains=query)
                | Q(location__icontains=query)
                | Q(defects__icontains=query)
                | Q(re_insp_fee__icontains=query)
            ).distinct()
        return super().get_queryset()


class InspectionDetailView(DetailView):
    model = Inspection


class InspectionCreateView(CreateView):
    model = Inspection
    form_class = InspectionForm


class InspectionUpdateView(UpdateView):
    model = Inspection
    form_class = InspectionForm
