# Generated by Django 3.1.3 on 2020-11-27 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcarts', '0073_productorder_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shippingaddress',
            field=models.TextField(blank=True, null=True),
        ),
    ]
