# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-12 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jportal', '0007_remove_jobseekers_designation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseekersprofile',
            name='education',
        ),
        migrations.AddField(
            model_name='jobseekersprofile',
            name='designation',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
