# Generated by Django 3.1.3 on 2020-11-21 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcarts', '0060_auto_20201119_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='dp/'),
        ),
    ]
