from django.urls import path
from .views import ProductListView, ProductCreateView


urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("create-product/", ProductCreateView.as_view(), name="create-product"),
]
