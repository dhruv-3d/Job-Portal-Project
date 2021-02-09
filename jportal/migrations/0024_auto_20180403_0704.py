# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-03 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jportal', '0023_auto_20180403_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseekersprofile',
            name='current_drawn_sal',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='jobseekersprofile',
            name='key_skills',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='jobseekersprofile',
            name='linkedin_profile',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobseekersprofile',
            name='pref_job_loc',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobseekersprofile',
            name='resume',
            field=models.FileField(blank=True, default='', null=True, upload_to='resume'),
        ),
        migrations.AlterField(
            model_name='jobseekersprofile',
            name='total_workexp',
            field=models.CharField(default='', max_length=20, null=True),
        ),
    ]