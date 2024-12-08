# Generated by Django 5.0.7 on 2024-12-08 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_activity_unit_alter_activity_activity_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='carbon_emissions',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(choices=[('transportation', 'Transportation'), ('energy', 'Energy'), ('water', 'Water'), ('waste', 'Waste')], max_length=50),
        ),
        migrations.AlterField(
            model_name='activity',
            name='unit',
            field=models.CharField(max_length=20),
        ),
    ]
