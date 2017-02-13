# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-13 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0002_auto_20170206_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='Calories',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cafe',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='cafe',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='cafe',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
