# Generated by Django 3.1 on 2020-11-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20201126_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetsinfo',
            name='asset_return',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
