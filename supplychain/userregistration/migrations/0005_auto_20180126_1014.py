# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-26 18:14
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userregistration', '0004_auto_20180126_1005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='manufacturer',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
