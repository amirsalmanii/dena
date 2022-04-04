from django.contrib import admin
from . import models

admin.site.register(models.NewsCategory)
admin.site.register(models.News)