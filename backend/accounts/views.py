import datetime
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from . import serializers
from .models import User


class MyPagination(PageNumberPagination):
    page_size = 20


class SetUser(APIView):
    """
    set user some data to frontend
    """
    def get(self, request):
        #token = request.COOKIES.get('token')
        #user = Token.objects.filter(key=token)
        user = request.user
        try:
            email = user.email
        except:
            return Response('user not found', status=401)
        else:
            #user = user.first()
            #user = user.user
            serializer = serializers.UserSerializer(user)
        
            
            return Response({"user_data":serializer.data}, status=200)
        return Response("user not found", status=401) 


class LoginUserView(APIView):
    def post(self, request):
        max_age = 365 * 24 * 60 * 60
        serializer = serializers.LoginSerializer(data=request.data)
        expires = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)
            if user:
                serializer = serializers.UserSerializer(user)
                try:
                    have_token = Token.objects.get(user=user)
                except:
                    user_token = Token.objects.create(user=user)
                    response = Response()
                    #response.set_cookie(key='token', value='user_token', httponly=True, expires=expires.strftime("%a, %d-%b-%Y %H:%M:%S UTC"), max_age=max_age, samesite='None', domain='127.0.0.1')
                    response.data = {
                        "token": f"{user_token}",
                        "user_data": serializer.data,
                    }
                    response.status_code = 200
                    return response
                else:
                    response = Response()
                    #response.set_cookie(key='token', value= have_token, httponly=True, expires=expires.strftime("%a, %d-%b-%Y %H:%M:%S UTC"), max_age=max_age)
                    response.data = {
                        "token": f"{have_token}",
                        "user_data": serializer.data,
                    }
                    print(have_token)
                    response.status_code = 200
                    return response
            else:
                return Response('رمز و ایمیل صحیح نمی باشد', status=400) # no user in system
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


class UsersListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    pagination_class = MyPagination


class AdminsListView(ListCreateAPIView):
    queryset = User.objects.filter(is_superuser=True)
    serializer_class = serializers.UserSerializer


class UserDetailUpdateView(APIView):
    def get(self, request, pk):
        user = User.objects.filter(id=pk)
        if user:
            user = user.first()
            serializer = serializers.UserDetailSerializer(user, context={'request': request})
            return Response(serializer.data, status=200)
        return Response(status=404)
    
    def put(self, request, pk):
        user = User.objects.filter(id=pk)
        if user:
            user = user.first()
            serializer = serializers.UserDetailSerializer(instance=user, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors, status=400)
        return Response(status=404)

    def delete(self, request, pk):
        user = User.objects.filter(id=pk)
        if user:
            user.delete()
            return Response(status=204)
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


class UserProfileDetail(APIView):
    def get(self, request):
        user = request.user
        if user.is_anonymous:
            return Response(status=404)
        serializer = serializers.UserDetailSerializer(user)
        return Response(serializer.data)


class UserTestA(APIView):
    def get(self, request):
        # print('+++++++++++++++++++++++++++++')
        print(request.COOKIES)
        token = request.COOKIES.get('token')
        return Response({'token': token})
