from django.db import models
from django.utils.translation import gettext_lazy as _


class PaymentMethodChoices(models.TextChoices):
    STRIPE = _("stripe"), _("Stripe")
    PAYPAL = _("paypal"), _("PayPal")
    PAYTM = _("paytm"), _("Paytm")
    CREDIT_CARD = _("credit_card"), _("Credit Card")


class StatusChoices(models.TextChoices):
    PENDING = _("pending"), _("Pending")
    PROCESSING = _("processing"), _("Processing")
    COMPLETED = _("paid"), _("Paid")
    CANCELLED = _("failed"), _("Failed")
