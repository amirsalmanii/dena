# Generated by Django 3.2 on 2022-07-08 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='rating',
            field=models.BigIntegerField(default=0),
        ),
    ]