# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-08 07:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jportal', '0003_auto_20180208_0707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appliers',
            old_name='job_id',
            new_name='job',
        ),
    ]
