from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mark
from .serializers import MarkSerializer


class UserMarksView(APIView):
    def get(self, request):
        try:
            user = request.user
            mark = Mark.objects.get(user=user)
            serializer = MarkSerializer(mark)
        except:
            return Response(status=400)
        else:
            return Response(serializer.data, status=200)
