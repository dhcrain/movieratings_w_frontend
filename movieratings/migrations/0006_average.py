# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0005_auto_20160611_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Average',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_rating', models.FloatField()),
                ('rating_count', models.IntegerField()),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieratings.Movie')),
            ],
        ),
    ]
