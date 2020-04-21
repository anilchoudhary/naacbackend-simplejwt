# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 05:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0002_auto_20170825_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='duration',
            field=models.CharField(max_length=100, verbose_name='Duration(in days)'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee', verbose_name='Employee ID'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='organization',
            field=models.CharField(max_length=100, verbose_name='Organization'),
        ),
    ]
