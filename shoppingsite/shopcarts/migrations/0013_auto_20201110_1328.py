# Generated by Django 3.1.3 on 2020-11-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcarts', '0012_auto_20201110_0535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='items',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='items',
            field=models.ManyToManyField(to='shopcarts.Product'),
        ),
    ]
