# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-02 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0022_auto_20191002_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='headline',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
