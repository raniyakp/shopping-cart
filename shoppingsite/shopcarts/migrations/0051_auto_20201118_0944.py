# Generated by Django 3.1.3 on 2020-11-18 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcarts', '0050_auto_20201118_0713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='ordered_at',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
