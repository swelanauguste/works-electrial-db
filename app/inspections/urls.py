from django.urls import path

from .views import (
    DefectCreateView,
    DefectDetailView,
    DefectListView,
    DefectUpdateView,
    InspectionApplicationCreateView,
    InspectionApplicationDetailView,
    InspectionApplicationListView,
    InspectionApplicationUpdateView,
    OfficerCreateView,
    OfficerDetailView,
    OfficerListView,
    OfficerUpdateView,
)

urlpatterns = [
    path(
        "",
        InspectionApplicationListView.as_view(),
        name="inspection-application-list",
    ),
    path(
        "inspection-application/detail/<int:pk>/",
        InspectionApplicationDetailView.as_view(),
        name="inspection-application-detail",
    ),
    path(
        "inspection-application/update/<int:pk>/",
        InspectionApplicationUpdateView.as_view(),
        name="inspection-application-update",
    ),
    path(
        "inspection-application/create/",
        InspectionApplicationCreateView.as_view(),
        name="inspection-application-create",
    ),
    #
    path("defects", DefectListView.as_view(), name="defect-list"),
    path("detail/<int:pk>/", DefectDetailView.as_view(), name="defect-detail"),
    path("create/", DefectCreateView.as_view(), name="defect-create"),
    path("update/<int:pk>/", DefectUpdateView.as_view(), name="defect-update"),
    #
    path("officers/", OfficerListView.as_view(), name="officer-list"),
    path(
        "officer/detail/<int:pk>/",
        OfficerDetailView.as_view(),
        name="officer-detail",
    ),
    path(
        "officer/update/<int:pk>/",
        OfficerUpdateView.as_view(),
        name="officer-update",
    ),
    path("officer/create/", OfficerCreateView.as_view(), name="officer-create"),
]
