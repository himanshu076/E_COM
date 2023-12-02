from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from cotegories.models import Category, Store
from utils.util import product_multi_image


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name="store_product"
    )
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name="category_product"
    )
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    # active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        value = self.name
        if not self.slug:
            self.slug = slugify(value, allow_unicode=True)
            super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Define the URL pattern for a single product detail view
        return reverse("product_detail", args=[str(self.id)])

    def is_available_in_stock(self):
        # Check if the product is available (quantity > 0)
        return self.quantity > 0

    def decrease_quantity(self, amount=1):
        # Decrease the quantity of the product
        if self.quantity >= amount:
            self.quantity -= amount
            self.save()

    def get_total_price(self):
        return self.price * self.quantity

    def get_category_name(self):
        return self.category.name

    def get_store_name(self):
        return self.store.name

    def get_description_preview(self, length=50):
        if len(self.description) <= length:
            return self.description
        else:
            return self.description[:length] + "..."

    def get_formatted_price(self):
        return "₹%.2f" % self.price

    def get_formatted_created_at(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S")

    def get_formatted_updated_at(self):
        return self.updated_at.strftime("%Y-%m-%d %H:%M:%S")


class ProductImage(models.Model):
    product = models.ManyToManyField(Product, related_name="images")
    image = models.ImageField(upload_to="media/product/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Product Images"
        # ordering = ["-id"]

    # def save(self, *args, **kwargs):
    #     breakpoint()
    #     if not self.id:  # Only set the upload path if the object is being created (not updated)
    #         self.image.upload_to = product_multi_image
    #     super().save(*args, **kwargs)

    def __str__(self):
        if self.product.count() > 1:
            return f"{self.product.count()} Product contains this image (Id {self.id})"
        else:
            return f"{self.product.count()} Products contains this image (Id {self.id})"

    def get_formatted_created_at(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S")

    def get_formatted_updated_at(self):
        return self.updated_at.strftime("%Y-%m-%d %H:%M:%S")


# class ProductAdditionalInfo(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='additional_info')
#     color = models.CharField(max_length=255)
#     material = models.CharField(max_length=255)
#     style = models.CharField(max_length=255)
#     rating = models.DecimalField(max_digits=3, decimal_places=1)
#     warranty_period = models.CharField(max_length=50)
#     country_of_origin = models.CharField(max_length=50)
#     manufacturer = models.CharField(max_length=100)
#     model_number = models.CharField(max_length=50)
#     release_date = models.DateField()
#     is_new_arrival = models.BooleanField(default=False)
#     is_discounted = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name_plural = 'Store Images'
#         # ordering = ["-id"]

#     def get_formatted_created_at(self):
#         return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

#     def get_formatted_updated_at(self):
#         return self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
