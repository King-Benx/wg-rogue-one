# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-08 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0008_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymuserconfig',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Shows status of Gym members'),
        ),
    ]
