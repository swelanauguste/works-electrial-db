from django.urls import path

from .views import (
    ReceiptsCreateView,
    ReceiptsDetailView,
    ReceiptsListView,
    ReceiptsUpdateView,
)

urlpatterns = [
    path("", ReceiptsListView.as_view(), name="receipt-list"),
    path("create/", ReceiptsCreateView.as_view(), name="receipt-create"),
    path("detail/<int:pk>/", ReceiptsDetailView.as_view(), name="receipt-detail"),
    path("update/<int:pk>/", ReceiptsUpdateView.as_view(), name="receipt-update"),
]
