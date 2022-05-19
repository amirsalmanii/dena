from rest_framework import serializers
from . import models


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        exclude = ("slug",)


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"
