from django import forms

from .models import Category, Electrical


class ElectricalForm(forms.ModelForm):
    class Meta:
        model = Electrical
        fields = "__all__"
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date"}),
            "i_date": forms.DateInput(attrs={"type": "date"}),
            "ex_date": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": "5"}),
        }
