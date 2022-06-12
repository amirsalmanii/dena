from django.urls import path
from . import views

urlpatterns = [
    # categories urls
    path("categories/", views.listCategoryView.as_view(), name="list_category"),
    path('categories-m2-wp/', views.ListCategories2WithoutPagination.as_view(), name='list_category2-without-pagination'),
    path("category/create/", views.CreateCategoryView.as_view(), name="create_category"),
    path("category/update/<int:pk>/", views.UpdateCategoryView.as_view(), name="detal_update_category"),
    path("category/delete/<int:pk>/", views.DeleteCategoryView.as_view(), name="delete_category"),
    # products urls
    path("products/", views.ProductsListView.as_view(), name="products_list"),
    path("products_wp/", views.ProductsListViewm2.as_view(), name="products_list_wp"),
    path("product/r/<int:pk>/", views.ProductsDetail.as_view(), name="products_detail"),
    path("product/create/", views.ProducCreatetView.as_view(), name="product_create"),
    path("product/d/<int:pk>/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("product/u/<int:pk>/", views.ProductUpdateView.as_view(), name="product_update"),
]
