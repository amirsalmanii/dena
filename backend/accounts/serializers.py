from rest_framework import serializers
from .models import User

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_null=False)
    password = serializers.CharField(max_length=200, allow_null=False)


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_null=False)
    password1 = serializers.CharField(max_length=200, allow_null=False)
    password2 = serializers.CharField(max_length=200, allow_null=False)

    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError('هر دو رمز باید برابر باشند')
        elif len(password1) <= 7:
            raise serializers.ValidationError('رمز باید هشت رقم باشد')
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'groups', 'user_permissions', 'date_joined', 'last_login', 'is_active')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'groups', 'user_permissions', 'date_joined', 'last_login', 'is_active')
        