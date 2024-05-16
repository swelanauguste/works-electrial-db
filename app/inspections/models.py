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
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="posts", null=True, blank=True
    )
    licence_no = models.CharField(max_length=100, null=True, blank=True)
    office = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="offices",
        null=True,
        blank=True,
    )
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    # log_sheet = models.FileField(
    #     upload_to="inspections/log_sheets/", null=True, blank=True
    # )
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("inspector-detail", kwargs={"pk": self.pk})

    def __str__(self):
        if self.licence_no:
            return f"{self.name.title()}({self.licence_no.upper()})"
        return f"{self.name.title()}({self.post.name.upper()})"


class InspectionDailyLog(models.Model):
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
        ("special", "Special"),
    ]

    week_choices = [
        ("week1", "Week 1"),
        ("week2", "Week 2"),
        ("week3", "Week 3"),
        ("week4", "Week 4"),
        ("week5", "Week 5"),
    ]
    date = models.DateField()
    zone = models.CharField(max_length=100, choices=zone_choices)
    vehicle = models.CharField(max_length=8, choices=vehicle_choices)
    start = models.TimeField()
    location = models.CharField(max_length=255)
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
        Inspector, on_delete=models.CASCADE, related_name="assistants"
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
    wireman = models.ForeignKey(
        Wireman,
        on_delete=models.CASCADE,
        related_name="wiremen",
        verbose_name="wireman/contactor",
        null=True,
        blank=True,
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
        return f"Application number#{self.app_no}"


class InspectionApplication(models.Model):
    inspection_type_choices = [
        ("new", "New"),
        ("alteration", "Alteration"),
        ("extension", "Extension"),
        ("reconnection", "Reconnection"),
    ]
    nature_of_work_choices = [
        ("dom", "Domestic"),
        ("com", "Commercial"),
        ("temp", "Temporary"),
        ("rout", "Routine"),
    ]
    zone_choices = [
        ("1", "One"),
        ("2", "Two"),
        ("3", "Three"),
    ]
    date = models.DateField()
    app_no = models.CharField(max_length=5, verbose_name="application number")
    receipt_no = models.CharField(max_length=10, verbose_name="receipt number")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    cert_no = models.CharField(max_length=10, verbose_name="certificate number")
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    zone = models.CharField(max_length=1, choices=zone_choices, null=True, blank=True)
    contactor = models.ForeignKey(
        Inspector,
        on_delete=models.CASCADE,
        related_name="contractors",
        null=True,
        blank=True,
    )
    lights = models.IntegerField(default=0, blank=True, null=True)
    sockets = models.IntegerField(default=0, blank=True, null=True)
    switches = models.IntegerField(default=0, blank=True, null=True)
    BC = models.IntegerField(default=0, blank=True, null=True)
    LE = models.FloatField(default=0, blank=True, null=True)
    LN = models.FloatField(default=0, blank=True, null=True)
    EN = models.FloatField(default=0, blank=True, null=True)
    AE = models.FloatField(default=0, blank=True, null=True)
    ins_type = models.CharField(
        max_length=15,
        choices=nature_of_work_choices,
        verbose_name="inspection type",
        blank=True,
        null=True,
    )
    mA = models.IntegerField(default=0, blank=True, null=True)
    sub_circuit = models.IntegerField(default=0, blank=True, null=True)
    main_rating = models.IntegerField(default=0, blank=True, null=True)
    inspector = models.ManyToManyField(Inspector, related_name="app_inspectors")
    assistant = models.ManyToManyField(Inspector, related_name="app_assistants")
    inspection_date = models.DateField()
    collected_by = models.CharField(max_length=100, blank=True, null=True)
    date_collected = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # owner = models.CharField(max_length=100, blank=True, null=True)
    # owner_address = models.TextField(blank=True, null=True, verbose_name="owner's address")
    # location = models.TextField()
    # nature_of_work = models.CharField(max_length=20, choices=nature_of_work_choices)
    # points = models.IntegerField()
    # contactor_address = models.TextField()
    # contactor_licence_no = models.CharField(
    #     max_length=100, verbose_name="licence number"
    # )
    file = models.FileField(
        upload_to="inspections/applications/", blank=True, null=True
    )

    def get_absolute_url(self):
        return reverse("inspection-application-detail", kwargs={"pk": self.pk})

    def get_total(self):
        return self.lights + self.sockets + self.switches

    def __str__(self):
        return f"Application number#{self.app_no}"
