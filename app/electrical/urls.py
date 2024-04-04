from django.urls import path

from .views import (
    ElectricalCreateView,
    ElectricalDetailView,
    ElectricalListView,
    ElectricalUpdateView,
)

urlpatterns = [
    path("", ElectricalListView.as_view(), name="electrical-list"),
    path("create/", ElectricalCreateView.as_view(), name="electrical-create"),
    path("detail/<int:pk>/", ElectricalDetailView.as_view(), name="electrical-detail"),
    path("update/<int:pk>/", ElectricalUpdateView.as_view(), name="electrical-update"),
]
