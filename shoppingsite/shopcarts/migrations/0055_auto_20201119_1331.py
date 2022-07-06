# Generated by Django 3.1.3 on 2020-11-19 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopcarts', '0054_auto_20201119_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cartproduct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shopcarts.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='shopcarts.Product'),
        ),
    ]
