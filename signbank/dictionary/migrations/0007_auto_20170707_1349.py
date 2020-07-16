# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-07 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0006_auto_20170628_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simultaneousmorphologydefinition',
            name='morpheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='glosses_containing', to='dictionary.Morpheme'),
        ),
        migrations.AlterField(
            model_name='simultaneousmorphologydefinition',
            name='parent_gloss',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='simultaneous_morphology', to='dictionary.Gloss'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_used_language',
            field=models.CharField(default='en', max_length=20),
        ),
    ]
