# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-02 17:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0021_auto_20191002_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='event',
            new_name='events',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='project',
            new_name='projects',
        ),
    ]
