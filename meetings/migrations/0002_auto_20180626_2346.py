# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 23:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CellForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.Cell')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.Cell')),
            ],
        ),
        migrations.RemoveField(
            model_name='objectives',
            name='cell',
        ),
        migrations.DeleteModel(
            name='Objectives',
        ),
    ]
