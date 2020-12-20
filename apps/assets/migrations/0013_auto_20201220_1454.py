# Generated by Django 3.1 on 2020-12-20 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0012_recommendedassetstobuy_date_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetschecklimits',
            name='potential_percent',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assetschecklimits',
            name='url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='assetschecklimits',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assetschecklimits',
            name='value_objective',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
