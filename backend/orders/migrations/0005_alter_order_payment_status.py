# Generated by Django 3.2 on 2022-06-26 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('p', 'payed'), ('r', 'refund')], default=('ds', 'دریافت سفارش'), max_length=1, null=True),
        ),
    ]
