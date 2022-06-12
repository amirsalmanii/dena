from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.ListCreateClubView.as_view(), name='list_create_club_memebers'),
    path('members/<int:pk>/', views.DetalUpdateDeleteClubView.as_view(), name='list_create_club_memebers'),
]