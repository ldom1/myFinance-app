# Generated by Django 2.2.7 on 2019-12-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pea', '0011_order_risk'),
    ]

    operations = [
        migrations.AddField(
            model_name='pea',
            name='varation',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
