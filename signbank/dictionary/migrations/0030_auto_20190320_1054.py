# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-20 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0029_auto_20181128_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='reference',
            field=models.TextField(blank=True))
    ]
