from django.urls import path

from .views import (
    WiremanCreateView,
    WiremanDetailView,
    WiremanListView,
    WiremanUpdateView,
)

urlpatterns = [
    path("", WiremanListView.as_view(), name="wireman-list"),
    path("create/", WiremanCreateView.as_view(), name="wireman-create"),
    path("detail/<int:pk>/", WiremanDetailView.as_view(), name="wireman-detail"),
    path("update/<int:pk>/", WiremanUpdateView.as_view(), name="wireman-update"),
]
