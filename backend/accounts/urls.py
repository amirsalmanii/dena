from django.urls import path
from . import views


urlpatterns = [
    path('login/user/', views.LoginUserView.as_view(), name='login_user'),
    path('register/user/', views.RegisterUserView.as_view(), name='register_user'),
    path('create/user/', views.CreateUserView.as_view(), name='create_user'),
    path('users/', views.UsersListView.as_view(), name='users_list'),
    path('user/<int:pk>/', views.UserDetailUpdateView.as_view(), name='user_detail_update'),
]