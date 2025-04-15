from django.urls import path
from .views import ProductListView, ProductCreateView, ProductRetrieveView, ProductDestroyView, OrderDeleteView, CreateOrderView, OrderRetrieveView


urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("create-product/", ProductCreateView.as_view(), name="create-product"),
    path("details-product/<int:pk>", ProductRetrieveView.as_view(), name="details-product"),
    path("delete-product/<int:pk>", ProductDestroyView.as_view(), name="delete-product"),
    path("delete-order/<int:pk>", OrderDeleteView.as_view(), name="delete-order"),
    path("order-details/<int:pk>", OrderRetrieveView.as_view(), name="order-details"),
    path("create-order/", CreateOrderView.as_view(), name="create-order"),
    
    
]
