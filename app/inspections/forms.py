from django import forms

from .models import Inspection

class InspectionForm(forms.ModelForm):
    class Meta:
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
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "insp_date": forms.DateInput(attrs={"type": "date"}),
        }