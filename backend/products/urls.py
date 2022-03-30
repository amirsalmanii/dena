from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.listCategoryView.as_view(), name='list_category'),
    path('create/category/', views.CreateCategoryView.as_view(), name='create_category'),
    path('update/category/<int:pk>/', views.UpdateCategoryView.as_view(), name='detal_update_category'),
    path('delete/category/<int:pk>/', views.DeleteCategoryView.as_view(), name='delete_category'),
]