# Generated by Django 3.1.3 on 2020-11-18 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopcarts', '0051_auto_20201118_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='price',
        ),
    ]
