# Generated by Django 4.2.20 on 2025-03-14 05:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('layouts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='faq',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='termsandconditions',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='termsandconditions',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
