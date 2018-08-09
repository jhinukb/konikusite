# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-03 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0016_auto_20180803_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='content_val',
            field=models.TextField(default='def val'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='file_location',
            field=models.CharField(default='file val', max_length=500),
        ),
        migrations.AddField(
            model_name='meeting',
            name='validate',
            field=models.CharField(choices=[('valid_nocom', 'Validated without comment'), ('valid_com', 'Validated with comments'), ('no_val', 'Cannot yet be validated')], default='val', max_length=500),
        ),
    ]