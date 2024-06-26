from django.db import models
from django.urls import reverse


class Location(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("location-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name.upper()}"


class Post(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name.upper()}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Officer(models.Model):
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
    notes = models.TextField(blank=True, null=True)
    photo = models.FileField(upload_to="electrical/photo/", null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    signature = models.FileField(
        upload_to="electrical/signature/", null=True, blank=True
    )
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
        return reverse("officer-detail", kwargs={"pk": self.pk})

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
        ("south", "South"),
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
    officer = models.ForeignKey(
        Officer,
        on_delete=models.CASCADE,
        related_name="officers",
        null=True,
        blank=True,
    )
    assistant = models.ForeignKey(
        Officer,
        on_delete=models.CASCADE,
        related_name="assistants",
        null=True,
        blank=True,
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
    officer = models.ForeignKey(
        Officer,
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
    INSTALLATION_TYPE_CHOICES = [
        ("1P", "1Phase"),
        ("3P", "3Phase"),
    ]
    nature_of_work_choices = [
        ("dom", "Domestic"),
        ("com", "Commercial"),
        ("temp", "Temporary"),
        ("rout", "Routine"),
        ("perd", "Periodic"),
    ]
    ZONE_CHOICES = [
        ("north", "North"),
        ("central", "Central"),
        ("east/west", "East/West"),
        ("south", "South"),
        ("special", "Special"),
    ]
    date = models.DateField(blank=True, null=True)
    job_no = models.CharField(max_length=5, verbose_name="application number")
    receipt_no = models.CharField(max_length=10, verbose_name="receipt number")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    cert_no = models.CharField(max_length=10, verbose_name="certificate number")
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    zone = models.CharField(max_length=10, choices=ZONE_CHOICES, null=True, blank=True)
    contractor = models.ForeignKey(
        Officer,
        on_delete=models.CASCADE,
        related_name="contractors",
        null=True,
        blank=True,
    )
    lights = models.IntegerField(default=0, blank=True, null=True)
    sockets = models.IntegerField(default=0, blank=True, null=True)
    switches = models.IntegerField(default=0, blank=True, null=True)
    inst_type = models.CharField(
        max_length=6,
        choices=INSTALLATION_TYPE_CHOICES,
        null=True,
        blank=True,
        help_text="Installation Phase Type",
    )
    LN = models.FloatField(default=0, blank=True, null=True)
    NE = models.FloatField(default=0, blank=True, null=True)
    LE = models.FloatField(default=0, blank=True, null=True)
    L1_L3 = models.FloatField(default=0, blank=True, null=True)
    L3_L2 = models.FloatField(default=0, blank=True, null=True)
    L1_L2 = models.FloatField(default=0, blank=True, null=True)
    L1_L3_L2_N = models.FloatField(default=0, blank=True, null=True)
    L1_L3_L2_E = models.FloatField(default=0, blank=True, null=True)
    E = models.FloatField(default=0, blank=True, null=True)
    EN = models.FloatField(default=0, blank=True, null=True)
    RE = models.FloatField(default=0, blank=True, null=True)
    kW = models.FloatField(default=0, blank=True, null=True)
    next_inspection = models.DateField(blank=True, null=True)
    CT_RT = models.CharField(max_length=100, blank=True, null=True)
    insp_type = models.CharField(
        max_length=15,
        choices=nature_of_work_choices,
        verbose_name="inspection type",
        blank=True,
        null=True,
    )
    mA = models.IntegerField(default=0, blank=True, null=True)
    sub_circuit = models.IntegerField(default=0, blank=True, null=True)
    main_rating = models.IntegerField(default=0, blank=True, null=True)
    inspector = models.ManyToManyField(
        Officer, related_name="app_inspectors", blank=True
    )
    assistant = models.ManyToManyField(
        Officer, related_name="app_assistants", blank=True
    )
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
