# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-21 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piaowu', '0005_wxuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='YuhuataiPerson',
            fields=[
                ('card_id', models.CharField(db_index=True, max_length=18)),
                ('visit_date', models.DateField(default=None)),
                ('people_number', models.IntegerField(default=None)),
                ('user_uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='YuhuataiTeam',
            fields=[
                ('card_id', models.CharField(db_index=True, max_length=18)),
                ('visit_date', models.DateField(default=None)),
                ('people_number', models.IntegerField(default=None)),
                ('user_uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
            ],
        ),
    ]