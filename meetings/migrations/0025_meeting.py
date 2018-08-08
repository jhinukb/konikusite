# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-06 22:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0024_auto_20180806_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendee_list', models.BooleanField(default=False)),
                ('date_recorded', models.DateTimeField(default=django.utils.timezone.now)),
                ('next_meeting_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.Cell')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.Member')),
            ],
        ),
    ]
