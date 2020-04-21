# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20171025_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='amnt_sanctioned',
            field=models.IntegerField(verbose_name='Amount Sanctioned'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='sponsors',
            field=models.TextField(verbose_name='Sponsoring Agency'),
        ),
    ]
