from django.urls import path

from order_management.views import PaymentView
from payment.views import PaymentListAPIView

urlpatterns = [
    path("payment/", PaymentView.as_view(), name="payment"),
    path("payment/list/", PaymentListAPIView.as_view(), name="payment"),
]
