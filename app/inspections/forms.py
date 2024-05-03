from django import forms

from .models import Defect

class DefectForm(forms.ModelForm):
    class Meta:
        model = Defect
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