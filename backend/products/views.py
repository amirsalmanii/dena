from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response
from . import serializers
from . import models

# categories views


class CreateCategoryView(CreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CreateCategorySerializer


class listCategoryView(ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoriesSerializer


class ListCategories2WithoutPagination(ListAPIView):
    """
    gives all categories
    good for admin panel
    """
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoriesSerializer


class UpdateCategoryView(RetrieveUpdateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CreateCategorySerializer


class DeleteCategoryView(DestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CreateCategorySerializer


# products views


class ProductsListView(ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductsDetailUpdateView(RetrieveUpdateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class CreateProductView(CreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductCreateSerializer


class ProductDeleteView(APIView):
    def delete(self, request, pk):
        try:
            product = models.Product.objects.get(id=pk)
        except:
            return Response(status=404)
        else:
            product.hide = True
            product.save()
            return Response(status=204)
