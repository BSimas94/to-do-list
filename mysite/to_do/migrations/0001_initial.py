# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-16 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('description', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
