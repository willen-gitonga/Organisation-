# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-09-29 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0017_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Future_plans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='DEFAULT VALUE', upload_to='photos/')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=150, null=True)),
                ('location', models.CharField(max_length=50)),
                ('time_taken', models.CharField(max_length=20)),
            ],
        ),
    ]
