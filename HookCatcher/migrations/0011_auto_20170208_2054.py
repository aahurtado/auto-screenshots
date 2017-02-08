# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HookCatcher', '0010_auto_20170208_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='git_branch_name',
            new_name='git_source_name',
        ),
        migrations.RemoveField(
            model_name='diff',
            name='source_state_img',
        ),
        migrations.RemoveField(
            model_name='diff',
            name='target_state_img',
        ),
        migrations.RemoveField(
            model_name='state',
            name='git_pr_number',
        ),
        migrations.AddField(
            model_name='diff',
            name='after_state_img',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='_isAfterState', to='HookCatcher.Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diff',
            name='before_state_img',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='_isBeforeState', to='HookCatcher.Image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diff',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='state',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
