from django.db import models


class Club(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    age = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    car = models.CharField(max_length=200, null=True, blank=True)
    license_cart = models.ImageField(upload_to='license/', null=True, blank=True)
    car_image = models.ImageField(upload_to='cars/', null=True, blank=True)

    class Meta:
        ordering = ("-id",)
