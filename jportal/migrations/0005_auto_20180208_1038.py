# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-08 10:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jportal', '0004_auto_20180208_0729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appliers',
            old_name='applier',
            new_name='jobseeker',
        ),
    ]
