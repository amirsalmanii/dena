from django.contrib import admin
from .models import Order, RefundOrdersRequest, OrderItems

admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(RefundOrdersRequest)