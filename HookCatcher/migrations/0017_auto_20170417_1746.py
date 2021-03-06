# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-17 17:46
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HookCatcher', '0016_auto_20170410_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='pr',
            name='gitPRCommit',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='prCommit_set', to='HookCatcher.Commit'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pr',
            name='gitSourceCommit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sourceCommit_set', to='HookCatcher.Commit'),
        ),
        migrations.AlterField(
            model_name='pr',
            name='gitTargetCommit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targetCommit_set', to='HookCatcher.Commit'),
        ),
    ]
