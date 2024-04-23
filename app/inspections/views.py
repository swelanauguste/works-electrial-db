from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Inspection


class InspectionListView(ListView):
    model = Inspection
    ordering = ["-date"]


class InspectionDetailView(DetailView):
    model = Inspection


class InspectionCreateView(CreateView):
    model = Inspection
    fields = [
        "sheet_no",
        "date",
        "app_no",
        "app_name",
        "inspector",
        "location",
        "insp_date",
        "defects",
        "re_insp_fee",
    ]


class InspectionUpdateView(UpdateView):
    model = Inspection
    fields = [
        "sheet_no",
        "date",
        "app_no",
        "app_name",
        "inspector",
        "location",
        "insp_date",
        "defects",
        "re_insp_fee",
    ]
