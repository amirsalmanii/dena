from rest_framework import serializers
from . import models
from tags.serializers import TagsSerializer

class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        exclude = ("slug",)


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = [
            "id",
            "name",
            "slug",
        ]


class ProductSerializer(serializers.ModelSerializer):
    categories = CreateCategorySerializer()
    tag = TagsSerializer()

    class Meta:
        model = models.Product
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"
