# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-01 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0013_auto_20180731_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='workreview',
            name='content_val',
            field=models.TextField(default='def val'),
        ),
    ]