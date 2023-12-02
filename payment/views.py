from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination

from payment.models import Payment
from payment.serializers import PaymentListSerializers


# Create your views here.
class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentListSerializers
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = PageNumberPagination
    page_size = 1
