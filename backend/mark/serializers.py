from rest_framework import serializers
from . import models


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mark
        fields = '__all__'
