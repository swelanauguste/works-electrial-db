from django import forms

from .models import Category, Wireman


class WiremanForm(forms.ModelForm):
    class Meta:
        model = Wireman
        fields = "__all__"
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date"}),
            "i_date": forms.DateInput(attrs={"type": "date"}),
            "ex_date": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": "5"}),
        }
