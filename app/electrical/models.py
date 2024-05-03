from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Wireman(models.Model):
    photo = models.FileField(upload_to="electrical/photo/", null=True, blank=True)
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    signature = models.FileField(
        upload_to="electrical/signature/", null=True, blank=True
    )
    license_no = models.CharField(max_length=5, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    i_date = models.DateField(verbose_name="Issued Date", null=True, blank=True)
    ex_date = models.DateField(verbose_name="Expired Date", null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    stamp = models.FileField(upload_to="electrical/stamp/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("electrical-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name}(#{self.license_no})"
