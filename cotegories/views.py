from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from cotegories.models import Category, Store, StoreImage
from cotegories.serializers import (CreateCategorySerializer,
                                    ListCategorySerializer,
                                    MultipleCategorySerializer,
                                    StoreSerializer)

# Create your views here.


# Category Related Views starts here.
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ListCategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CreateCategorySerializer


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = ListCategorySerializer


class MultipleCategoryCreateView(generics.CreateAPIView):
    serializer_class = MultipleCategorySerializer

    def create(self, request, *args, **kwargs):
        category_list = request.data.get("category_list", [])
        Category.create_categories(category_list)
        return Response(
            {"message": "Multiple Categories & Sub-Categories created successfully"},
            status=status.HTTP_201_CREATED,
        )


# Category Related Views end here.


# Store Related Views starts here.
class StoreListCreateView(generics.ListCreateAPIView):
    """
    *Example, How to Create Store using Json Format or called Schema
    {
    "store_owner": 1,
    "store_name": "Test Store",
    "store_tagline": "Store tagline",
    "store_about_us": "About the store",
    "store_images": [
        {
            "image": "image_data_1"
        },
        {
            "image": "image_data_2"
        }
        ]
    }
    """

    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


# Store Related Views starts here.
