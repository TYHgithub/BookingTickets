# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-27 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piaowu', '0006_yuhuataiperson_yuhuataiteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='wxuser',
            name='status',
            field=models.PositiveIntegerField(default=0, verbose_name='\u7968\u52a1\u72b6\u6001'),
        ),
    ]