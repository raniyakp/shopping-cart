# Generated by Django 3.1.3 on 2020-11-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcarts', '0039_auto_20201116_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(null=True, to='shopcarts.CartItem'),
        ),
    ]
