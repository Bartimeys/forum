# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-29 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20160824_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
