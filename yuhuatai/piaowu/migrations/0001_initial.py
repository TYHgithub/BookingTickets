# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YuhuataiUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=18)),
                ('telephone_number', models.CharField(max_length=11)),
                ('user_uuid', models.CharField(max_length=18)),
                ('register_date', models.DateField()),
            ],
        ),
    ]
