from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Tag
from .serializers import TagsSerializer


class ListTagsView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer


class ListTagsView2(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer


class DetailDeleteUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer
