from django.contrib import admin

from .models import (
    Defect,
    InspectionApplication,
    InspectionDailyLog,
    Officer,
    Location,
    Post,
    Category
)

admin.site.register(Defect)
admin.site.register(InspectionDailyLog)
admin.site.register(Officer)
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(InspectionApplication)
admin.site.register(Category)

