# Generated by Django 2.2.7 on 2019-11-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds_CA', '0002_auto_20191125_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundsca',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
