from rest_framework import serializers
from .models import Order, OrderItems, RefundOrdersRequest
from accounts.serializers import UserSerializer
from products.serializers import ProductCreateSerializer


class OrderSerializerM1(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class OrderSerializerM2(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderSerializerM3(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('owner',)


class OrderItemsSerializerM1(serializers.ModelSerializer):
    product = ProductCreateSerializer()
    class Meta:
        model = OrderItems
        fields = '__all__'


class OrdersItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItems
        fields = '__all__'


class OrderRefundsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = RefundOrdersRequest
        fields = '__all__'


class OrderRefundUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = RefundOrdersRequest
        fields = '__all__'


class OrderRefundUpdateSerializer2(serializers.ModelSerializer):
    class Meta:
        model = RefundOrdersRequest
        exclude = ('user',)
