# Generated by Django 3.1 on 2020-11-08 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20201108_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optimassetsinfo',
            name='previously_selected',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
