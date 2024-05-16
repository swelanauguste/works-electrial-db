from django.contrib import admin

from .models import (
    Defect,
    InspectionApplication,
    InspectionDailyLog,
    Inspector,
    Location,
    Post,
)

admin.site.register(Defect)
admin.site.register(InspectionDailyLog)
admin.site.register(Inspector)
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(InspectionApplication)
