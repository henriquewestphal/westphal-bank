# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-09 11:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0005_auto_20180209_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conta',
            name='limite',
        ),
    ]
