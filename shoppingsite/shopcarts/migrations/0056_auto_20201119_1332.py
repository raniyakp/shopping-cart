# Generated by Django 3.1.3 on 2020-11-19 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopcarts', '0055_auto_20201119_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='cartproduct',
            new_name='product',
        ),
    ]
