from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from cotegories.models import Category, Store, StoreImage

# Register your models here.


class CategoryAdmin(DraggableMPTTAdmin):
    # list_display = ['id', 'name', 'parent', 'slug', 'description']
    # list_display_links = None
    prepopulated_fields = {"slug": ("name",)}


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'author', 'slug', 'price',
#                         'in_stock', 'created', 'updated']
#     list_filter = ['in_stock', 'is_active']
#     prepopulated_fields = {'slug': ('title',)}


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ["store_owner", "store_name", "store_tagline", "created"]
    # prepopulated_fields = {'slug': ('name',)}


@admin.register(StoreImage)
class StoreImageAdmin(admin.ModelAdmin):
    list_display = ["id"]


admin.site.register(Category, CategoryAdmin)
