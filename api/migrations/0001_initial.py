# Generated by Django 4.1.1 on 2022-10-01 17:18

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('desc', models.TextField(default='', max_length=100)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('foods', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('desc', models.TextField(default='', max_length=100)),
                ('owner', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='api.restaurant')),
            ],
        ),
    ]
