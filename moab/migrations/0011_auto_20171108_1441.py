# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-08 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moab', '0010_auto_20171107_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='type',
            field=models.CharField(max_length=100, verbose_name='Membership Type'),
        ),
    ]
