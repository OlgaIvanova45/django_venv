from rest_framework import generics
from ..models import Products
from .serializers import ProductsSerializer


class ProductListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer