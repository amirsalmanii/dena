from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from . import serializers
from . import models


class CreateCategoryView(CreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CreateCategorySerializer


class listCategoryView(ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoriesSerializer


class UpdateCategoryView(RetrieveUpdateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CreateCategorySerializer


class DeleteCategoryView(DestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CreateCategorySerializer
