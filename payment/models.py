from django.db import models
from django.utils import timezone

from order_management.models import Order
from payment.constant import PaymentMethodChoices, StatusChoices


# Create your models here.
class Payment(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_payment"
    )
    payment_id = models.CharField(max_length=50, editable=False, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    payment_method = models.CharField(
        max_length=20, choices=PaymentMethodChoices.choices
    )
    transaction_status = models.CharField(
        max_length=20, choices=StatusChoices.choices, default=StatusChoices.PENDING
    )
    created = models.DateTimeField(auto_now_add=True)

    # Stripe-specific Fields
    stripe_charge_id = models.CharField(max_length=50)
    stripe_customer_id = models.CharField(max_length=50)
    card_last4 = models.CharField(max_length=4)
    card_brand = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Payments"
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        if not self.payment_id:
            prefix = "PAY"
            timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
            last_order = Payment.objects.order_by("id").last()
            sequential_number = (last_order.id + 1) if last_order else 1
            self.payment_id = f"{prefix}-{timestamp}-{sequential_number:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.payment_id} {self.id}"

    def is_transaction_completed(self):
        return self.transaction_status == StatusChoices.COMPLETED
