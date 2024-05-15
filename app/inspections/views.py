from django.db.models import Q
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import DefectForm
from .models import Defect, Inspection


class InspectionListView(ListView):
    model = Inspection
    ordering = ["-date"]

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Inspection.objects.filter(
                Q(zone__icontains=query)
                | Q(vehicle__icontains=query)
                | Q(size__name__icontains=query)
                | Q(job_no__icontains=query)
                | Q(appl__icontains=query)
                | Q(test_data__icontains=query)
                | Q(status__icontains=query)
                | Q(inspector__name__icontains=query)
                | Q(assistance__name__icontains=query)
            ).distinct()
        return super().get_queryset()


class InspectionDetailView(DetailView):
    model = Inspection


class InspectionCreateView(CreateView):
    model = Inspection
    fields = "__all__"


class InspectionUpdateView(UpdateView):
    model = Inspection
    fields = "__all__"


class DefectListView(ListView):
    model = Defect
    ordering = ["-date"]

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Defect.objects.filter(
                Q(sheet_no__icontains=query)
                | Q(app_no__icontains=query)
                | Q(inspector__name__icontains=query)
                | Q(location__icontains=query)
                | Q(defects__icontains=query)
                | Q(re_insp_fee__icontains=query)
            ).distinct()
        return super().get_queryset()


class DefectDetailView(DetailView):
    model = Defect


class DefectCreateView(CreateView):
    model = Defect
    form_class = DefectForm


class DefectUpdateView(UpdateView):
    model = Defect
    form_class = DefectForm
