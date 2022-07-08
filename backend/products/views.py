from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response
from rest_framework import filters
from url_filter.integrations.drf import DjangoFilterBackend
from . import serializers
from . import models
from accounts.views import MyPagination


class CreateCategoryView(CreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CreateCategorySerializer


class listCategoryView(ListAPIView):
    pagination_class = MyPagination
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoriesSerializer


class ListCategories2WithoutPagination(ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoriesSerializer


class UpdateCategoryView(RetrieveUpdateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CreateCategorySerializer


class DeleteCategoryView(DestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CreateCategorySerializer


# products_views

class ProductsListView(ListAPIView):
    pagination_class = MyPagination
    queryset = models.Product.objects.filter(hide=False)
    serializer_class = serializers.ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    filter_fields = ['tag', 'categories']


class ProductsListViewm2(ListAPIView):
    queryset = models.Product.objects.filter(hide=False)
    serializer_class = serializers.ProductSerializer


class LastProductsListView(ListAPIView):
    queryset = models.Product.objects.filter(hide=False)[:15]
    serializer_class = serializers.ProductSerializer


class ProductsDetail(RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProducCreatetView(CreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductCreateSerializer


class ProductUpdateView(UpdateAPIView):
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
