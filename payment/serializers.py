from rest_framework import serializers

from payment.models import Payment


class PaymentListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        read_only_fields = ["id"]
        depth = 10
