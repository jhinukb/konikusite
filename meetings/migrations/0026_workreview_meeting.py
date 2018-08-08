# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-06 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0025_meeting'),
    ]

    operations = [
        migrations.AddField(
            model_name='workreview',
            name='meeting',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meetings.Meeting'),
        ),
    ]
