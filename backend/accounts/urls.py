from django.urls import path
from . import views


urlpatterns = [
    path('set_user', views.SetUser.as_view(), name='user_data'),
    path('login/user/', views.LoginUserView.as_view(), name='login_user'),
    path('register/user/', views.RegisterUserView.as_view(), name='register_user'),
    path('users/', views.UsersListView.as_view(), name='users_list'),
    path('users/a/', views.AdminsListView.as_view(), name='users_list'),
    path('user/<int:pk>/', views.UserDetailUpdateView.as_view(), name='user_detail_update'),
    path('user/forget/', views.ForgetPassword.as_view(), name='update_user_password'),
    path('usertest/', views.UserTestA.as_view(), name='user_tst'),
]
