# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 19:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0004_auto_20160611_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='average',
            name='movie_id',
        ),
        migrations.DeleteModel(
            name='Average',
        ),
    ]