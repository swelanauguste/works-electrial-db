from django.urls import path

from .views import (
    InspectionCreateView,
    InspectionDetailView,
    InspectionListView,
    InspectionUpdateView,
)

urlpatterns = [
    path("", InspectionListView.as_view(), name="inspection-list"),
    path("detail/<int:pk>/", InspectionDetailView.as_view(), name="inspection-detail"),
    path("create/", InspectionCreateView.as_view(), name="inspection-create"),
    path("update/<int:pk>/", InspectionUpdateView.as_view(), name="inspection-update"),
]
