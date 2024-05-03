from django.db import models
from django.urls import reverse
from electrical.models import Wireman


class Location(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("location-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name}"


class Inspector(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")
    office = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="offices"
    )
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    log_sheet = models.FileField(
        upload_to="inspections/log_sheets/", null=True, blank=True
    )
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("inspector-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name}({self.email})"


class Inspection(models.Model):
    vehicle_choices = [
        ("private", "Private"),
        ("SLG", "SLG"),
    ]
    status_choices = [
        ("fail", "Fail"),
        ("pass", "Pass"),
    ]
    zone_choices = [
        ("north", "North"),
        ("central", "Central"),
        ("east/west", "East/West"),
    ]
    Inspection_type_choices = [
        ("domestic", "Domestic"),
        ("commercial", "Commercial"),
        ("temporary", "Temporary"),
        ("routine", "Routine"),
    ]
    week_choices = [
        ('week1', 'Week 1'),
        ('week2', 'Week 2'),
        ('week3', 'Week 3'),
        ('week4', 'Week 4'),
        ('week5', 'Week 5'),
        
    ]
    date = models.DateField()
    zone = models.CharField(max_length=100)
    vehicle = models.CharField(max_length=8, choices=vehicle_choices)
    start = models.TimeField()
    localtion = models.CharField(max_length=255)
    size = models.CharField(max_length=10)
    job_no = models.CharField(max_length=10)
    appl = models.CharField(max_length=5)
    test_data = models.CharField(max_length=255)
    status = models.CharField(max_length=4, choices=status_choices)
    end = models.TimeField()
    inspector = models.ForeignKey(
        Inspector, on_delete=models.CASCADE, related_name="inspectors"
    )
    assistant = models.ForeignKey(
        Inspector, on_delete=models.CASCADE, related_name="inspectors"
    )

    def get_absolute_url(self):
        return reverse("inspection-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.job_no}"


class Defect(models.Model):
    sheet_no = models.IntegerField(unique=True, null=True)
    date = models.DateField()
    app_no = models.CharField(max_length=5, verbose_name="application number")
    app_name = models.CharField(max_length=100, verbose_name="applicant's name")
    inspector = models.ForeignKey(
        Inspector, on_delete=models.CASCADE, related_name="wiremen"
    )
    location = models.CharField(max_length=255)
    insp_date = models.DateField(verbose_name="inspection date")
    defects = models.TextField()
    re_insp_fee = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="re-inspection fee"
    )
    defect_sheet = models.FileField(upload_to="inspections/defect_sheet/", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("inspection-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.app_no}"
