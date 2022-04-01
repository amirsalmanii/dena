from django.urls import path
from . import views

urlpatterns = [
    # categories urls
    path("categories/", views.listCategoryView.as_view(), name="list_category"),
    path(
        "category/create/", views.CreateCategoryView.as_view(), name="create_category"
    ),
    path(
        "category/update/<int:pk>/",
        views.UpdateCategoryView.as_view(),
        name="detal_update_category",
    ),
    path(
        "category/delete/<int:pk>/",
        views.DeleteCategoryView.as_view(),
        name="delete_category",
    ),
    # products urls
    path("products/", views.ProductsListView.as_view(), name="products_list"),
    path(
        "product/<int:pk>/",
        views.ProductsDetailUpdateView.as_view(),
        name="products_detail_update",
    ),
    path("product/create/", views.CreateProductView.as_view(), name="product_create"),
    path(
        "product/delete/<int:pk>/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
]
