from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .models import Club
from .serializers import ClubSerializer
from accounts.views import MyPagination


class ListCreateClubView(ListCreateAPIView):
    pagination_class = MyPagination
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class DetalUpdateDeleteClubView(RetrieveDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
