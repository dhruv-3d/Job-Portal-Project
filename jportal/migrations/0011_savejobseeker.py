# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-15 05:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jportal', '0010_auto_20180314_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveJobseeker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='jportal.Employer')),
                ('jobseeker', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='jportal.JobSeekers')),
            ],
        ),
    ]
