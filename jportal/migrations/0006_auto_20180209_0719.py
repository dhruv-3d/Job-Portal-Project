# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-09 07:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jportal', '0005_auto_20180208_1038'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmployerProfile',
            new_name='EmployerCompanyProfile',
        ),
    ]