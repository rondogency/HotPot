# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-29 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pic', models.ImageField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('description', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
