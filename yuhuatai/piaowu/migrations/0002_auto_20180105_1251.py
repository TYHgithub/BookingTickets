# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piaowu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yuhuataiuser',
            name='user_uuid',
            field=models.CharField(max_length=36),
        ),
    ]
