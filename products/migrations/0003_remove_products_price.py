# Generated by Django 2.0 on 2019-07-08 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190708_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
    ]
