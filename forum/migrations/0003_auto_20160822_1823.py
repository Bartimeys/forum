# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-22 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_category_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='forum.Topic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='forum.Category'),
            preserve_default=False,
        ),
    ]