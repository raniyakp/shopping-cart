# Generated by Django 3.1.3 on 2020-11-15 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcarts', '0029_auto_20201114_0453'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='ordered_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]