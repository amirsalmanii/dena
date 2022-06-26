from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, ListAPIView
from rest_framework.response import Response
from .models import Mark
from . import serializers
from products.models import Product


class UserMarksView(ListAPIView):
    serializer_class = serializers.MarkSerializer

    def get_queryset(self):
        marks = Mark.objects.filter(user=self.request.user)
        return marks


class DeleteMarkView(DestroyAPIView):
    queryset = Mark.objects.all()
    serializer_class = serializers.MarkSerializer


class RemoveOrAddToMarksView(APIView):
    def get(self, request, pk):
        user = request.user
        product = get_object_or_404(Product, id=pk)
        if user.is_authenticated:
            is_rel = Mark.objects.filter(user=user, product=product)
            if is_rel:
                is_rel = is_rel.first()
                is_rel.delete()
                return Response(status=204)
            Mark.objects.create(user=user, product=product)
            return Response(status=200)
        return Response(status=404)