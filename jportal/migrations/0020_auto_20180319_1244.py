# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-19 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jportal', '0019_auto_20180319_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banners_category',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
