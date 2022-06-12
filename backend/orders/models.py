from uuid import uuid4
from datetime import date
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
from django.dispatch import receiver
from products.models import Product
from accounts.models import User


class Order(models.Model):
    PAYMENT_STATUS = (
        ("p", "payed"), # w --> waited
        ("r", "refund")
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='order')
    payment_status = models.CharField(choices=PAYMENT_STATUS, max_length=20)
    total_price = models.BigIntegerField(null=True, blank=True)
    confirmation = models.BooleanField(default=False)
    payment_date = models.DateField(blank=True, null=True)
    order_id = models.UUIDField(default=uuid4)

    def __str__(self):
        return f'{str(self.owner)}'

    class Meta:
        ordering = ['-id']


@receiver(pre_save, sender=Order)
def set_amount(sender, instance, *args, **kwargs):
    # when client payed order we set time
    if instance.payment_status == 'p':
        instance.payment_date = date.today()


class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # frontend send
    product_price = models.PositiveBigIntegerField() # frontend send
    product_company_price = models.BigIntegerField(default=0)
    total_product_company_price = models.PositiveBigIntegerField(null=True, blank=True)
    total_amount = models.PositiveBigIntegerField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0) # frontend send
    order_id = models.UUIDField(null=True, blank=True) # frontend send

    def save(self, *args, **kwargs):
        self.product_company_price = self.product.company_price
        self.total_product_company_price = self.product.company_price * self.quantity
        self.total_amount = self.product_price * self.quantity
        super(OrderItems, self).save(*args, **kwargs)


@receiver(post_save, sender=OrderItems)
def set_quntity(sender, instance, *args, **kwargs):
    """
    this method
    If they buy products from the threat of buying
    that product, the total number in the warehouse will be reduced
    """
    value_of_product = instance.product.repository_quantity
    value_of_product -= instance.quantity
    if value_of_product >= 0:
        instance.product.repository_quantity = value_of_product
        instance.product.save()
    elif value_of_product < 0:
        instance.product.repository_quantity = 0
        instance.product.save()


class RefundOrdersRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='refunds')
    order_id = models.UUIDField()
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    Confirmation = models.BooleanField(default=False)

    class Meta:
        ordering = ('-id',)


@receiver(post_save, sender=RefundOrdersRequest)
def set_refund(sender, instance, *args, **kwargs):
    """
    when admin set confirmation true wen set this order status to refund
    """
    if instance.Confirmation == True:
        orderid = instance.order_id
        exists = Order.objects.filter(order_id=orderid)
        if exists:
            order = exists.first()
            order.payment_status = 'r'
            order.save()
    else:
        pass
