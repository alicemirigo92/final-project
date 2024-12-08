# Generated by Django 5.0.7 on 2024-12-05 13:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_badge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badge',
            name='earned_at',
        ),
        migrations.AddField(
            model_name='activity',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='badge',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]