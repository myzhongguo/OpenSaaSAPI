# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-10 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='api_cache',
            fields=[
                ('rowid', models.AutoField(primary_key=True, serialize=False)),
                ('inserttm', models.DateTimeField()),
                ('digest', models.CharField(max_length=512)),
                ('appkey', models.CharField(max_length=512)),
                ('api_id', models.CharField(max_length=512)),
                ('params', models.TextField()),
                ('data', models.TextField()),
                ('enable', models.IntegerField()),
            ],
        ),
    ]
