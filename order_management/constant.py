from django.db import models

STATUS_MAPPING = {
    "pending": "pending",
    "paid": "processing",
    "failed": "cancelled",
}
