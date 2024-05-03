from django.db.models import Q
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import DefectForm
from .models import Defect


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
