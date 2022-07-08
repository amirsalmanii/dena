from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, UpdateAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework import filters
from .models import Order, OrderItems, RefundOrdersRequest
from . import serializers
from accounts.views import MyPagination


class ListOrdersView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializerM1
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['order_id', 'owner__first_name', 'owner__last_name', 'owner__username']


class CreateOrderView(APIView):
    def post(self, request):
        serializer = serializers.OrderSerializerM3(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data['order_id'], status=200)
        return Response(serializer.errors, status=400)


class OrderItemsCreateView(APIView):
    def post(self, request):
        serializer = serializers.OrdersItemCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class RestriveOrdersView(APIView):
    def get(self, request, order_id):
        order = Order.objects.get(order_id=order_id)
        order_items = OrderItems.objects.filter(order_id=order_id)

        serializer_order = serializers.OrderSerializerM1(order)
        serializer_order_items = serializers.OrderItemsSerializerM1(order_items, context={'request': request},
                                                                    many=True)
        return Response({'data_1': serializer_order.data, 'data_2': serializer_order_items.data}, status=200)

    def put(self, request, order_id):
        order = Order.objects.get(order_id=order_id)
        serializer = serializers.OrderSerializerM2(instance=order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        return Response(serializer.errors, status=400)


class RefundsOrdersRequestView(ListAPIView):
    queryset = RefundOrdersRequest.objects.all()
    serializer_class = serializers.OrderRefundsSerializer
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__last_name', 'user__username', 'order_id']


class RefundOrderRequestDetailDeleteView(RetrieveDestroyAPIView):
    queryset = RefundOrdersRequest.objects.all()
    serializer_class = serializers.OrderRefundsSerializer


class RefundOrderRequestUpdateView(UpdateAPIView):
    queryset = RefundOrdersRequest.objects.all()
    serializer_class = serializers.OrderRefundUpdateSerializer


class RefundRequestCreate(APIView):
    def post(self, request):
        serializer = serializers.OrderRefundUpdateSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(status=200)
        return Response(serializer.errors, status=400)


class UserOrders(ListAPIView):
    serializer_class = serializers.OrderSerializerM1

    def get_queryset(self):
        user = self.request.user
        q = Order.objects.filter(owner=user)
        return q