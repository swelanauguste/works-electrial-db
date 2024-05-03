from django.urls import path

from .views import DefectCreateView, DefectDetailView, DefectListView, DefectUpdateView

urlpatterns = [
    path("", DefectListView.as_view(), name="defect-list"),
    path("detail/<int:pk>/", DefectDetailView.as_view(), name="defect-detail"),
    path("create/", DefectCreateView.as_view(), name="defect-create"),
    path("update/<int:pk>/", DefectUpdateView.as_view(), name="defect-update"),
]
