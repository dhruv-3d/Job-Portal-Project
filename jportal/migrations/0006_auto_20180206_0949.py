# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-06 09:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jportal', '0005_auto_20180206_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='city',
            new_name='state',
        ),
    ]
