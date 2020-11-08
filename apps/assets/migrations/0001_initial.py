# Generated by Django 3.1 on 2020-11-08 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('id_asset', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.URLField(blank=True, max_length=300, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('value', models.FloatField(blank=True, null=True)),
                ('variation', models.FloatField(blank=True, null=True)),
                ('ouverture', models.FloatField(blank=True, null=True)),
                ('cloture_veille', models.FloatField(blank=True, null=True)),
                ('haut', models.FloatField(blank=True, null=True)),
                ('bas', models.FloatField(blank=True, null=True)),
                ('volume', models.FloatField(blank=True, null=True)),
                ('dividende', models.FloatField(blank=True, null=True)),
                ('date_dividende', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AssetsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_update', models.DateTimeField(blank=True, null=True)),
                ('id_asset', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('value', models.FloatField(blank=True, null=True)),
                ('variation', models.FloatField(blank=True, null=True)),
                ('dividende', models.FloatField(blank=True, null=True)),
                ('value_3_month', models.FloatField(blank=True, null=True)),
                ('value_1_month', models.FloatField(blank=True, null=True)),
                ('value_1_week', models.FloatField(blank=True, null=True)),
                ('var_3_month', models.FloatField(blank=True, null=True)),
                ('var_1_month', models.FloatField(blank=True, null=True)),
                ('var_1_week', models.FloatField(blank=True, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
