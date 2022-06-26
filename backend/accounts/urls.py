from django.urls import path
from . import views


urlpatterns = [
    path('login/user/', views.LoginUserView.as_view(), name='login_user'),
    path('register/user/', views.RegisterUserView.as_view(), name='register_user'),
    path('users/', views.UsersListView.as_view(), name='users_list'),
    path('users/a/', views.AdminsListView.as_view(), name='users_list'),
    path('user/<int:pk>/', views.UserDetailUpdateView.as_view(), name='user_detail_update'),
    path('user/forget/', views.ForgetPassword.as_view(), name='update_user_password'),
    path('user/profile/', views.UserProfileDetail.as_view(), name='user_profile_detail'),
]