from datetime import datetime

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

from accounts.models import User
from utils.util import store_multi_image

# Create your models here.
# class Tag(models.Model):
#     name = models.CharField(max_length=255)


class Store(models.Model):
    store_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="store_owner"
    )
    store_name = models.CharField(max_length=115, unique=True)
    store_tagline = models.CharField(max_length=155)
    store_about_us = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Stores"
        ordering = ["-created"]

    def __str__(self):
        return "{} {}".format(self.store_name, self.id)

    @property
    def store_with_owner(self):
        return Store.objects.select_related("store_owner").get(pk=self.pk)

    @property
    def store_with_logo(self):
        return Store.objects.prefetch_related("store_logo").get(pk=self.pk)


class StoreImage(models.Model):
    image = models.ImageField(upload_to=store_multi_image)
    # tags = models.ManyToManyField('Tag')
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name="store_images"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Store Images"
        # ordering = ["-id"]

    def __str__(self):
        return "{} (Id {})".format(self.store.store_name, self.id)


class Category(MPTTModel):
    name = models.CharField(max_length=settings.CATEGORY_MAX_LENGTH, unique=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    slug = models.SlugField(
        max_length=settings.CATEGORY_MAX_LENGTH, null=True, blank=True
    )
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        suffix = super().__str__()
        return "{} {}".format(self.name, self.id)

    def save(self, *args, **kwargs):
        value = self.name
        if not self.slug:
            self.slug = slugify(value, allow_unicode=True)
            super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("items-by-category", args=[str(self.slug)])

    @classmethod
    def create_categories(cls, category_list):
        """
        # Usage
        category_paths = ["Toys & Games > Toys > Sports Toys > American Football Toys",
                                "Toys & Games > Toys > Sports Toys > Baseball Toys",
                                "Toys & Games > Toys > Sports Toys > Basketball Toys",
                                "Toys & Games > Toys > Sports Toys > Boomerangs",
                                "Toys & Games > Toys > Sports Toys > Bowling Toys",]

        Category.create_categories(category_paths)
        """
        for category_path in category_list:
            categories = category_path.split(" > ")
            parent = None
            for name in categories:
                category, created = cls.objects.get_or_create(name=name, parent=parent)
                parent = category
