from django.urls import path

from products import views

urlpatterns = [
    # product views starts here.
    path("list/", views.ProductListAPIView.as_view(), name="product-list"),
    path("create/", views.ProductCreateAPIView.as_view(), name="product-create"),
    path(
        "<int:pk>/",
        views.ProductRetrieveUpdateDestroyAPIView.as_view(),
        name="product-detail-update-delete",
    ),
    # product views end here.
    # ---------------------------------------------------------------------------------------------------------
    # Store views starts here.
    # Store views end here.
]
