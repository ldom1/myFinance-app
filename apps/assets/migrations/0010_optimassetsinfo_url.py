# Generated by Django 3.1 on 2020-11-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0009_auto_20201127_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='optimassetsinfo',
            name='url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
