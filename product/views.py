from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from product.models import Product, Category, Order, OrderItem
from .serializers import ProductSerializer, ProductDeleteSerializer
from rest_framework.permissions import AllowAny



class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [AllowAny]



class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()



class ProductRetrieveView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()



class ProductDestroyView(DestroyAPIView):
    serializer_class = ProductDeleteSerializer
    queryset = Product.objects.all()



