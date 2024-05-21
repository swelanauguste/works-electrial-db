from django import forms

from .models import Defect, InspectionApplication, Officer


class OfficerForm(forms.ModelForm):
    class Meta:
        model = Officer
        fields = "__all__"
        # widgets = {
        #     "date_collected": forms.DateInput(attrs={"type": "date"}),
        #     "date": forms.DateInput(attrs={"type": "date"}),
        #     "inspection_date": forms.DateInput(attrs={"type": "date"}),
        # }


class InspectionApplicationForm(forms.ModelForm):
    class Meta:
        model = InspectionApplication
        fields = "__all__"
        widgets = {
            "date_collected": forms.DateInput(attrs={"type": "date"}),
            "date": forms.DateInput(attrs={"type": "date"}),
            "inspection_date": forms.DateInput(attrs={"type": "date"}),
        }


class DefectForm(forms.ModelForm):
    class Meta:
        model = Defect
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "insp_date": forms.DateInput(attrs={"type": "date"}),
        }
