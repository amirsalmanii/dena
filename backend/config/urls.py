from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('accounts.urls')),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('news.urls')),
    path('api/v1/', include('tags.urls')),
    path('api/v1/', include('orders.urls')),
    path('api/v1/', include('discount.urls')),
    path('api/v1/', include('club.urls')),
    path('api/v1/', include('mark.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

