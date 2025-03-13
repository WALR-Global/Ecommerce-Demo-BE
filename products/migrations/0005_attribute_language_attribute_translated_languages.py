# Generated by Django 4.2.20 on 2025-03-13 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_attribute_created_at_attribute_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='language',
            field=models.CharField(blank=True, default='en', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='attribute',
            name='translated_languages',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
