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
    InspectorCreateView,
    InspectorDetailView,
    InspectorListView,
    InspectorUpdateView,
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
    path("inspectors/", InspectorListView.as_view(), name="inspector-list"),
    path(
        "inspector/detail/<int:pk>/",
        InspectorDetailView.as_view(),
        name="inspector-detail",
    ),
    path(
        "inspector/update/<int:pk>/",
        InspectorUpdateView.as_view(),
        name="inspector-update",
    ),
    path("inspector/create/", InspectorCreateView.as_view(), name="inspector-create"),
]
