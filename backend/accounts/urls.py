from django.urls import path
from . import views


urlpatterns = [
    path('login/user/', views.LoginUser.as_view(), name='login_user'),
    path('register/user/', views.RegisterUser.as_view(), name='register_user'),
]