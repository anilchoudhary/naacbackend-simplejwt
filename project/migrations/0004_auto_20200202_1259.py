# Generated by Django 3.0.2 on 2020-02-02 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0003_auto_20171025_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee_projects', to=settings.AUTH_USER_MODEL, verbose_name='Employee ID'),
        ),
    ]
