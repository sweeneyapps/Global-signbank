# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-18 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0022_auto_20180607_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='gloss',
            name='lemma',
            field=models.ForeignKey(null=True, on_delete=models.deletion.SET_NULL,
                                    to='dictionary.LemmaIdgloss'),
        ),
    ]
