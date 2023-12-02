from django.urls import path

from cotegories import views

urlpatterns = [
    # Category views starts here.
    path("categories/list/", views.CategoryListView.as_view(), name="category-list"),
    path(
        "categories/create/", views.CategoryCreateView.as_view(), name="category-create"
    ),
    path(
        "categories/detail/<int:pk>/",
        views.CategoryRetrieveUpdateDestroyView.as_view(),
        name="category-detail",
    ),
    path(
        "categories/create_multiple_categories/",
        views.MultipleCategoryCreateView.as_view(),
        name="create-multiple-categories",
    ),
    # Category views end here.
    # ---------------------------------------------------------------------------------------------------------
    # Store views starts here.
    path("stores/", views.StoreListCreateView.as_view(), name="store-list"),
    path(
        "stores/<int:pk>/", views.StoreRetrieveUpdateView.as_view(), name="store-detail"
    ),
    # Store views end here.
]
