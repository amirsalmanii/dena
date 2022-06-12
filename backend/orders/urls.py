from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.ListOrdersView.as_view(), name='orders_list'),
    path('order/create/', views.CreateOrderView.as_view(), name='orders_create'),
    path('orders/item/create/', views.OrderItemsCreateView.as_view(), name='orders_items'),
    path('order/<str:order_id>/', views.RestriveOrdersView.as_view(), name='orders_create'),
    path('refunds/', views.RefundsOrdersRequestView.as_view(), name='refund_list'),
    path('refunds/<int:pk>/', views.RefundOrderRequestDetailDeleteView.as_view(), name='refund_detail_delete'),
    path('refunds/u/<int:pk>/', views.RefundOrderRequestUpdateView.as_view(), name='refund_update'),
    path('profile/orders/', views.UserOrders.as_view(), name='profile_orders'),
    path('refund/c/', views.RefundRequestCreate.as_view(), name='refund_create'),
]