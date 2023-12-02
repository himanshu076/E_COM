from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import authentication, filters, generics, permissions

from products.models import Product
from products.paginations import TenToHUndredPagination
from products.serializers import ProductCreateSerializer, ProductListSerializer
# from products.permissions import IsOwnerOrReadOnly
from utils.permissions import IsOwner, IsOwnerOrReadOnly

# Create your views here.


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = TenToHUndredPagination
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly. IsOwner]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name", "sku", "store", "category", "description"]
    ordering_fields = ["price"]
    filterset_fields = {
        "category": ["exact"],
        "store": ["exact"],
        "is_featured": ["exact"],
        "is_available": ["exact"],
    }


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
