# Generated by Django 4.2.20 on 2025-03-14 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_manufacturer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
    ]
