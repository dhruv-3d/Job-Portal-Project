# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-26 05:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('jportal', '0010_auto_20180224_0711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='name',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='name',
            new_name='state',
        ),
        migrations.AlterField(
            model_name='depend',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='jportal.City'),
        ),
        migrations.AlterField(
            model_name='depend',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jportal.State'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='jportal.City'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jportal.State'),
        ),
        migrations.AlterField(
            model_name='jobseekers',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='jportal.City'),
        ),
        migrations.AlterField(
            model_name='jobseekers',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jportal.State'),
        ),
    ]
