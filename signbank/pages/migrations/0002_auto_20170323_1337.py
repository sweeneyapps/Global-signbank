# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagevideo',
            name='video',
            field=models.FileField(blank=True, upload_to='pages'),
        ),
    ]
