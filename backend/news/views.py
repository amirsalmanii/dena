from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from . import serializers, models


class ListNewsCategoryCreateView(ListCreateAPIView):
    queryset = models.NewsCategory.objects.all()
    serializer_class = serializers.NewsCategorySerializer


class NewsCategoryUpdateDetailDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.NewsCategory.objects.all()
    serializer_class = serializers.NewsCategorySerializer


class ListNewsView(ListAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer


class CreateNewsView(CreateAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsCreateSerializer


class NewsUpdateDetailDestroyView(APIView):
    def get(self, request, pk):
        news = models.News.objects.filter(id=pk)
        if news:
            serializer = serializers.NewsSerializer(news.first())
            return Response(serializer.data, status=200)
        return Response(status=404)

    def put(self, request, pk):
        news = models.News.objects.filter(id=pk)
        if news:
            serializer = serializers.NewsCreateSerializer(data=request.data, instance=news.first())
            if serializer.is_valid():
                serializer.save()
                return Response(status=200)
            return Response(serializer.errors, status=400)
        return Response(status=404)

    def delete(self, request, pk):
        news = models.News.objects.filter(id=pk)
        if news:
            news = news.first()
            news.delete()
            return Response(status=204)
        return Response(status=404)
