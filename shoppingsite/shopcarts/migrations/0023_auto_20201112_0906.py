# Generated by Django 3.1.3 on 2020-11-12 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcarts', '0022_auto_20201111_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]