# Generated by Django 3.1.3 on 2020-11-26 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcarts', '0068_auto_20201126_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='shopcarts.Product'),
        ),
    ]
