from rest_framework import serializers


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