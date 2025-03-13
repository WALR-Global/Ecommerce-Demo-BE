# Generated by Django 4.2.20 on 2025-03-13 18:53

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_attribute_language_attribute_translated_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='translated_languages',
            field=models.JSONField(blank=True, default=products.models.default_translated_languages, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='translated_languages',
            field=models.JSONField(blank=True, default=products.models.default_translated_languages, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='translated_languages',
            field=models.JSONField(blank=True, default=products.models.default_translated_languages, null=True),
        ),
    ]
