from rest_framework import serializers
from .models import Tag


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'id')