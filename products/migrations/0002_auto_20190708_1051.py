# Generated by Django 2.0 on 2019-07-08 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='strore_id',
            new_name='store_id',
        ),
    ]