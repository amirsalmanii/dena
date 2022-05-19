from django.contrib import admin
from . import models


@admin.register(models.Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(models.Product)
class AdminCategory(admin.ModelAdmin):
    list_display = ["name", "price", "company_price", "hide"]
