# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-03 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0015_remove_workreview_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objective',
            name='cell',
        ),
        migrations.RemoveField(
            model_name='objective',
            name='cell_output',
        ),
        migrations.RemoveField(
            model_name='objective',
            name='changed_reason',
        ),
        migrations.RemoveField(
            model_name='objective',
            name='exp_obj_dt',
        ),
        migrations.RemoveField(
            model_name='objective',
            name='exp_supply_dt',
        ),
        migrations.RemoveField(
            model_name='objective',
            name='incompletion_reason',
        ),
        migrations.AlterField(
            model_name='objective',
            name='completion_status',
            field=models.CharField(choices=[('complete', 'complete'), ('incomplete', 'incomplete'), ('changed', 'changed')], max_length=400),
        ),
        migrations.AlterField(
            model_name='objective',
            name='objective_text',
            field=models.TextField(default='val'),
        ),
    ]
