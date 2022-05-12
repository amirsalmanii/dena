from django.db import models
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from products.models import Product
import jdatetime


class Discount(models.Model):
    products = models.ManyToManyField(Product, related_name='products')
    discount_percent = models.IntegerField(default=0)
    valid_from = models.DateField(blank=True, null=True)
    valid_to = models.DateField(blank=True, null=True)


@receiver(pre_save, sender=pre_save)
def change_date(sender, instance, *args, **kwargs):
    date_from = instance.valid_from
    date_to = instance.valid_to
    instance.valid_from = jdatetime.date(year=date_from.year, month=date_from.month, day=date_from.day).togregorian()
    instance.valid_to = jdatetime.date(year=date_to.year, month=date_to.month, day=date_to.day).togregorian()


@receiver(pre_delete, sender=Discount)
def delete_discount_from_products(sender, instance, *args, **kwargs):
    products = instance.products.all()
    for pr in products:
        pr.price_after_discount = 0
        pr.save()




