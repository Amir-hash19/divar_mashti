from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, ListCreateAPIView
from product.models import Product, Category, Order, OrderItem
from .serializers import ProductSerializer, ProductDeleteSerializer, OrderSerializer, OrderSerializerDetails
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from account.models import UserAccount



class ProductPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = "50"


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPagination
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["brand", "category", "price"]




class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

  



class ProductRetrieveView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()



class ProductDestroyView(DestroyAPIView):
    serializer_class = ProductDeleteSerializer
    queryset = Product.objects.all()




class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    


class CreateOrderView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
            serializer.save(
                 customer = self.request.user 
        )



class OrderRetrieveView(RetrieveAPIView):
    serializer_class = OrderSerializerDetails
    queryset = Order.objects.all()
    permission_classes = [AllowAny]