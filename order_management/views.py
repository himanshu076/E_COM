import os

import stripe
from django.db import transaction
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from order_management.serializers import OrderSerializer, PaymentSerializer

stripe.api_key = os.getenv("STRIPE_API_KEY")


# # Create your views here.
# class CheckoutView(APIView):
#     def post(self, request):
#         checkout_serializer = CheckoutSerializer(data=request.data)
#         # serializer = CheckoutSerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 # Perform transaction here
#                 order = serializer.save()
#                 return Response({"message": "Order placed successfully.", "order_id": order.id}, status=status.HTTP_201_CREATED)
#             except Exception as e:
#                 # Handle transaction failure and rollback
#                 return Response({"message": "Failed to place order. Please try again later."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AddToCartView(generics.CreateAPIView):
    def post(self, request):
        # Retrieve product data from the request
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        
        # Validate the product data and add it to the cart
        # Implement your logic here
        
        return Response({"message": "Product added to cart"}, status=status.HTTP_200_OK)
    

# class AddressListView(generics.ListCreateAPIView):
#     def get(self, request):
#         # Retrieve the user's addresses
#         addresses = Address.objects.filter(user=request.user)
#         serializer = AddressSerializer(addresses, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         # Create a new address
#         serializer = AddressSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PaymentView(generics.GenericAPIView):
    # queryset = Order.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderSerializer

    def post(self, request, format=None):
        payment = {}
        payment["card_number"] = request.data.get("payment.card_number")
        payment["expiration_month"] = request.data.get("payment.expiration_month")
        payment["expiration_year"] = request.data.get("payment.expiration_year")
        payment["cvc"] = request.data.get("payment.cvc")
        payment["amount"] = request.data.get("payment.amount")
        # payment['currency'] = request.data.get('payment.currency')

        order_serializer = OrderSerializer(
            data=request.data, context={"request": request}
        )
        payment_serializer = PaymentSerializer(
            data=payment, context={"request": request}
        )

        if order_serializer.is_valid() and payment_serializer.is_valid():
            with transaction.atomic():
                order = order_serializer.save()
                payment_serializer.context["order"] = order
                payment = payment_serializer.save()
                payment.save()
                order.payment_resference = payment.payment_id
                order.save()

            return Response(
                {
                    "order_id": order.order_id,
                    "message": "Your order successfully placed.",
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            errors = {}
            errors.update(order_serializer.errors)
            errors.update(payment_serializer.errors)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
