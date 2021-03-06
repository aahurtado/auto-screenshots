# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 23:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HookCatcher', '0011_auto_20170208_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diff',
            name='after_state_img',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='isAfterState', to='HookCatcher.Image'),
        ),
        migrations.AlterField(
            model_name='diff',
            name='before_state_img',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='isBeforeState', to='HookCatcher.Image'),
        ),
    ]
