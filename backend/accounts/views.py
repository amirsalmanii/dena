from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from . import serializers
from .models import User


class MyPagination(PageNumberPagination):
    page_size = 20


class LoginUserView(APIView):
    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)
            if user:
                try:
                    have_token = Token.objects.get(user=user)
                except:
                    user_token = Token.objects.create(user=user)
                    return Response({'token':user_token.key}, status=200)
                else:
                    return Response({'token':have_token.key}, status=200)
            else:
                return Response('رمز و ایمیل صحیح نمی باشد') # no user in system
        return Response(serializer.errors, status=400)


class RegisterUserView(APIView):
    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password2']
            user_exist = User.objects.filter(email=email)
            if not user_exist:
                user = User(email=email)
                user.set_password(password)
                user.save()
                return Response('created', status=201)
            return Response('کاربر قبلا وجود دارد', status=400)
        return Response(serializer.errors, status=400)


class UsersListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetailUpdateView(APIView):
    def get(self, request, pk):
        user = User.objects.filter(id=pk)
        if user:
            user = user.first()
            serializer = serializers.UserDetailSerializer(user)
            return Response(serializer.data, status=200)
        return Response(status=404)
    
    def put(self, request, pk):
        user = User.objects.filter(id=pk)
        if user:
            user = user.first()
            serializer = serializers.UserDetailSerializer(instance=user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors, status=400)
        return Response(status=404)


class ForgetPassword(APIView):
    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        '''
        از این سریالایزر برای دریافت ایمیل و رمز برای تغییر رمز استفاده شده
        '''
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password2']
            user = User.objects.filter(email=email)
            if user:
                user = user.first()
                user.set_password(password)
                user.save()
                return Response('رمز با موفقیت تغییر یافت', status=200)
            else:
                return Response(status=404)
        else:
            return Response(serializer.errors, status=400)
