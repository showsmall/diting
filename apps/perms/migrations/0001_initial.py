# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-13 09:14
from __future__ import unicode_literals

import common.utils
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('navis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaviPermission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('date_expired', models.DateTimeField(default=common.utils.date_expired_default, verbose_name='Date expired')),
                ('created_by', models.CharField(blank=True, max_length=128, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('navi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navis.Navi', verbose_name='Navi')),
            ],
            options={
                'verbose_name': 'Navi permission',
            },
        ),
    ]
