from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from order_management.constant import STATUS_MAPPING
from payment.constant import StatusChoices
from products.models import Product

# from payment.models import Payment

User = get_user_model()


# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_order")
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_resference = models.CharField(max_length=100, blank=True)
    # quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Orders"
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        if not self.order_id:
            # Generate the meaningful ID based on timestamp and sequential number
            timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
            last_order = Order.objects.order_by("id").last()
            sequential_number = (last_order.id + 1) if last_order else 1
            self.order_id = f"{timestamp}{sequential_number:04d}"
        super().save(*args, **kwargs)

    # @property
    # def order_status(self):
    #     payment = Payment.objects.filter(payment_reference=self.payment_resference).first()
    #     if payment:
    #         return STATUS_MAPPING.get(payment.transaction_status, 'pending')
    #     return 'pending'

    def is_payment_completed(self):
        return self.order_payment.filter(
            transaction_status=StatusChoices.COMPLETED
        ).exists()
