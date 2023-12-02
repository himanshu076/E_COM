import stripe
from rest_framework import serializers

from accounts.models import UserProfile
from order_management.models import Order
from payment.models import Payment

stripe.api_key = "sk_test_51NKJh1SHt14p3Ij3Da4co7G8HO3TbcoqDAU02YNYuWUt8sswVwR9UHtPC1nCWtzr4HCK51OcQdAKS0mKZQhcFWIl00GaIszwtA"  # Set your Stripe API key


# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = '__all__'
#         read_only_fields = ['id']


# class CheckoutSerializer(serializers.Serializer):
#     # order = OrderSerializer()
#     user_profile = UserProfileSerializer()
#     payment = PaymentSerializers()

#     class Meta:
#         model = Order
#         fields = '__all__'
#         read_only_fields = ['id']

# def create(self, validated_data):
#     order_data = validated_data.pop('order')
#     user_profile_data = validated_data.pop('user_profile')
#     payment_data = validated_data.pop('payment')
#     # payment_token = validated_data.pop('payment_token')
#     # address = validated_data.pop('address')

#     # Perform payment processing here
#     # If payment is successful, create Payment instance and save it
#     # Otherwise, raise an exception to trigger transaction rollback

#     # Create Payment instance
#     payment = Payment.objects.create(**validated_data)

#     # Assign payment reference to the order
#     order = Order.objects.create(**order_data)
#     order.payment_reference = payment.payment_id
#     order.save()

#     return order


def create_card_token(card_number, expiration_month, expiration_year, cvc):
    token = stripe.Token.create(
        card={
            "number": card_number,
            "exp_month": expiration_month,
            "exp_year": expiration_year,
            "cvc": cvc,
        }
    )
    return token.id


# Example usage
card_number = "4242424242424242"
expiration_month = 12
expiration_year = 2025
cvc = "123"


class PaymentSerializer(serializers.Serializer):
    card_number = serializers.CharField(max_length=16)
    expiration_month = serializers.IntegerField(min_value=1, max_value=12)
    expiration_year = serializers.IntegerField(min_value=2023)
    cvc = serializers.CharField(max_length=4)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    # currency = serializers.CharField(max_length=3, default='usd')

    # class Meta:
    #     read_only_fields = ['currency']

    def create(self, validated_data):
        # Create a Stripe payment charge
        # breakpoint()
        card_number = validated_data["card_number"]
        expiration_month = validated_data["expiration_month"]
        expiration_year = validated_data["expiration_year"]
        cvc = validated_data["cvc"]
        amount = validated_data["amount"]
        currency = "usd"

        # Use the test card details provided by Stripe for testing purposes
        test_card_number = "4242424242424242"
        test_exp_month = 12
        test_exp_year = 2024
        test_cvc = "123"

        try:
            intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),  # Convert amount to cents
                currency=currency,
                # payment_method_data={
                #     'type': 'card',
                #     'card': {
                #         'number': card_number,
                #         'exp_month': expiration_month,
                #         'exp_year': expiration_year,
                #         'cvc': cvc,
                #     },
                # },
                payment_method="pm_card_visa",
            )
        except stripe.error.CardError as e:
            # Handle card error
            raise serializers.ValidationError(str(e))
        except stripe.error.InvalidRequestError as e:
            # Handle invalid request error
            raise serializers.ValidationError(str(e))

        card_details = stripe.PaymentMethod.retrieve(intent.payment_method).card
        customer_details = (
            stripe.Customer.retrieve(intent.customer) if intent.customer else None
        )

        # Create the payment object
        payment = Payment.objects.create(
            order=self.context.get("order"),
            amount=amount,
            currency=currency,
            payment_method="stripe",
            transaction_status="completed",
            stripe_charge_id=intent.id,
            stripe_customer_id=customer_details.customer
            if customer_details
            else "7481dvsfd_47",
            card_last4=card_details.last4,
            card_brand=card_details.brand,
        )
        return payment


class UserProfileAddressUpdate(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["address"]


class OrderSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer()

    # address = UserProfileAddressUpdate()
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ["order_id", "created", "payment_resference", "address"]

    def create(self, validated_data):
        request = self.context.get("request")
        # Get the payment object and update the payment_reference in the order
        payment = validated_data.pop("payment")
        # validated_data['payment_reference'] = payment.payment_id

        # try:
        #     address = request.user.user_profile.address
        # except:
        #     address = validated_data['address']
        #     user = request.user
        #     UserProfile.objects.filter(user=user).update(address=address)

        # Set the address instance in the validated data
        # validated_data['address'] = address

        # Update Address if not exist othervisen get
        # address = validated_data.pop('address')
        # user = request.user
        # UserProfile.objects.filter(user=user).update(address=address)

        # Create the order object
        total_amount = validated_data["total_amount"]
        # user = request.user
        user = validated_data["user"]
        products = validated_data["products"]

        order = Order.objects.create(user=user, total_amount=total_amount)
        order.products.set(products)

        return order
