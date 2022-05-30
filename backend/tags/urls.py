from django.urls import path
from . import views

urlpatterns = [
    path('tags/', views.ListTagsView.as_view(), name='tags_list'),
    path('tags_w_p/', views.ListTagsView2.as_view(), name='tags_list'),
    path('tag/<int:pk>/', views.DetailDeleteUpdateView.as_view(), name='tags_detail_delete_update'),
]