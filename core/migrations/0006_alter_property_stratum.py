# Generated by Django 5.1.7 on 2025-03-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_property_stratum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='stratum',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
