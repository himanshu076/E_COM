from django.contrib import admin

from products.models import Product, ProductImage


# Register your models here.
@admin.register(ProductImage)
class StoreAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class StoreAdmin(admin.ModelAdmin):
    list_display = ["name", "sku", "quantity", "created", "is_featured", "is_available"]
