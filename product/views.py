from rest_framework.generics import ListAPIView, CreateAPIView
from product.models import Product, Category, Order, OrderItem
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [AllowAny]



