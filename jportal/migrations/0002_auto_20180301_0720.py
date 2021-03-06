# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-01 07:20
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jportal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='company_name',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employer',
            name='designation',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employer',
            name='contact_no',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='employer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
