# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-11 03:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jportal', '0024_auto_20180403_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jportal.State'),
        ),
    ]
