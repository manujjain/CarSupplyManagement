# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-31 03:52
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('userregistration', '0005_auto_20180126_1014'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Manufacturer',
            new_name='UserRegistration',
        ),
        migrations.AlterModelManagers(
            name='userregistration',
            managers=[
                ('manufacturers', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
