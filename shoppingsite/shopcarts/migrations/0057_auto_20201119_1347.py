# Generated by Django 3.1.3 on 2020-11-19 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcarts', '0056_auto_20201119_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='shopcarts.CartItem'),
        ),
    ]