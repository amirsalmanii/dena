from rest_framework import serializers
from . import models
from tags.serializers import TagsSerializer
from mark.models import Mark

class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        exclude = ("slug",)


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = [
            "id",
            "image",
            "name",
            "slug",
        ]


class ProductSerializer(serializers.ModelSerializer):
    categories = CreateCategorySerializer()
    tag = TagsSerializer()
    is_fav = serializers.SerializerMethodField()

    def get_is_fav(self, instance):
        """
        check this product fav of user or not
        if fav send true else send false
        """
        user = self.context.get('request').user
        try:
            Mark.objects.get(user=user, product=instance)
        except:
            return False
        else:
            return True
    
    class Meta:
        model = models.Product
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"
