# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 07:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professional_details', '0006_auto_20170903_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professional',
            old_name='academic_experience',
            new_name='title',
        ),
    ]
