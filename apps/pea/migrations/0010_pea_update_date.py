# Generated by Django 2.2.7 on 2019-11-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pea', '0009_peahistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='pea',
            name='update_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]