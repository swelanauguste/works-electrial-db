from django import forms

from .models import Defect, InspectionApplication

class InspectionApplicationForm(forms.ModelForm):
    class Meta:
        model = InspectionApplication
        fields = '__all__'
        widgets = {
            "date_collected": forms.DateInput(attrs={"type": "date"}),
            "date": forms.DateInput(attrs={"type": "date"}),
            "inspection_date": forms.DateInput(attrs={"type": "date"}),
        }

class DefectForm(forms.ModelForm):
    class Meta:
        model = Defect
        fields = [
            "sheet_no",
            "date",
            "app_no",
            "app_name",
            "wireman",
            "location",
            "insp_date",
            "defects",
            "re_insp_fee",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "insp_date": forms.DateInput(attrs={"type": "date"}),
        }