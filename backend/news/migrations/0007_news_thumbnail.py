# Generated by Django 3.2 on 2022-06-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_news_summery'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='news/th/'),
        ),
    ]
