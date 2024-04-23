from django.db import models
from django.urls import reverse
from electrical.models import Electrical


class Receipts(models.Model):
    receipt_no = models.CharField(max_length=10)
    electrical = models.ForeignKey(
        Electrical, on_delete=models.CASCADE, related_name="receipts"
    )
    years = models.IntegerField(default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=202)
    date = models.DateField()
    # paid = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]

    def get_absolute_url(self):
        return reverse("receipt-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.electrical.name} - XCD${self.amount} - {self.date} - #{self.receipt_no}"
