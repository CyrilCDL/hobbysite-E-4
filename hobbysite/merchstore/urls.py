from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('items', ProductListView.as_view(), name="product_type"),
    path('item/<int:pk>', ProductDetailView.as_view(), name="product"),
    ]

app_name = "merchstore"