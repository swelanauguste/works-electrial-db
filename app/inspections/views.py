from django.db.models import Q
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import DefectForm, InspectionApplicationForm
from .models import Defect, InspectionApplication, InspectionDailyLog, Inspector


class InspectorListView(ListView):
    model = Inspector
    ordering = ["-created_at"]

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Inspector.objects.filter(
                Q(name__icontains=query)
                | Q(licence_no__icontains=query)
                | Q(email__icontains=query)
                | Q(phone__icontains=query)
                | Q(post__name__icontains=query)
                | Q(office__name__icontains=query)
            ).distinct()
        return super().get_queryset()


class InspectorDetailView(DetailView):
    model = Inspector


class InspectorCreateView(CreateView):
    model = Inspector
    fields = "__all__"


class InspectorUpdateView(UpdateView):
    model = Inspector
    fields = "__all__"


class InspectionApplicationListView(ListView):
    model = InspectionApplication
    ordering = ["-date"]

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return InspectionApplication.objects.filter(
                Q(app_no__icontains=query)
                | Q(receipt_no__icontains=query)
                | Q(cert_no__icontains=query)
                | Q(name__icontains=query)
                | Q(area__icontains=query)
                | Q(contactor__icontains=query)
                | Q(ins_type__icontains=query)
                | Q(collected_by__icontains=query)
                | Q(date_collected__icontains=query)
            ).distinct()
        return super().get_queryset()


class InspectionApplicationDetailView(DetailView):
    model = InspectionApplication


class InspectionApplicationCreateView(CreateView):
    model = InspectionApplication
    form_class = InspectionApplicationForm

    # success url to list view
    def get_success_url(self):
        return reverse("inspection-application-list")


class InspectionApplicationUpdateView(UpdateView):
    model = InspectionApplication
    form_class = InspectionApplicationForm


class InspectionDailyLogListView(ListView):
    model = InspectionDailyLog
    ordering = ["-date"]

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return InspectionDailyLog.objects.filter(
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


class InspectionDailyLogDetailView(DetailView):
    model = InspectionDailyLog


class InspectionDailyLogCreateView(CreateView):
    model = InspectionDailyLog
    fields = "__all__"


class InspectionDailyLogUpdateView(UpdateView):
    model = InspectionDailyLog
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
