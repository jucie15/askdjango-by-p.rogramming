# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
