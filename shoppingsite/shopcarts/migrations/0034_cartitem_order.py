# Generated by Django 3.1.3 on 2020-11-15 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopcarts', '0033_remove_cartitem_ordered_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopcarts.order'),
        ),
    ]
