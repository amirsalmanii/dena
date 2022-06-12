from django.urls import path
from . import views


urlpatterns = [
    path('news_categories/', views.ListNewsCategoryCreateView.as_view(), name='news_categories_list_create'),
    path('news_categories-wp/', views.ListNewsCategoryCreatem2View.as_view(), name='news_categories_list_create'),
    path('news_category/<int:pk>/', views.NewsCategoryUpdateDetailDestroyView.as_view(), name='news_category_update_detail_destroy'),
    path('news/', views.ListNewsView.as_view(), name='news_list'),
    path('news/create/', views.CreateNewsView.as_view(), name='news_create'),
    path('news/<int:pk>/', views.NewsUpdateDetailDestroyView.as_view(), name='news_create'),

]