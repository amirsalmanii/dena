# Generated by Django 3.2 on 2022-06-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
