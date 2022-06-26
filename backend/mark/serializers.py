from rest_framework import serializers
from . import models
from products.serializers import ProductCreateSerializer


class MarkSerializer(serializers.ModelSerializer):
    product = ProductCreateSerializer()

    class Meta:
        model = models.Mark
        fields = '__all__'
