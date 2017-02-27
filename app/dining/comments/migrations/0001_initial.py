# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-27 05:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('cafes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1300)),
                ('feedback', models.CharField(max_length=300)),
                ('date_written', models.DateTimeField(null=True)),
                ('rating', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
                ('meal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cafes.Cafe')),
            ],
        ),
    ]
