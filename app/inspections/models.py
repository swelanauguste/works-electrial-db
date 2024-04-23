from django.db import models
from django.urls import reverse
from electrical.models import Electrical as Inspector


class Inspection(models.Model):
    sheet_no = models.IntegerField(unique=True, null=True)
    date = models.DateField()
    app_no = models.CharField(max_length=5, verbose_name='application number')
    app_name = models.CharField(max_length=100, verbose_name="applicant's name")
    inspector = models.ForeignKey(
        Inspector, on_delete=models.CASCADE, related_name="wiremen"
    )
    location = models.CharField(max_length=255)
    insp_date = models.DateField(verbose_name="inspection date")
    defects = models.TextField()
    re_insp_fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="re-inspection fee")
    defect_sheet = models.FileField(upload_to="inspections/defect_sheet/", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("inspection-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.app_no}"
