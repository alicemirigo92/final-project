# Generated by Django 5.0.7 on 2024-12-08 12:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_remove_activity_emissions_remove_activity_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badge',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='badge',
            name='earned_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='badge',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
