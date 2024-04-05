from django import forms

from .models import Receipts


class ReceiptsForm(forms.ModelForm):
    class Meta:
        model = Receipts
        fields = "__all__"
        exclude = ["paid"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "i_date": forms.DateInput(attrs={"type": "date"}),
            "ex_date": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": "5"}),
        }
