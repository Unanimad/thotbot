# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-20 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20180220_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='arguments',
            field=models.TextField(blank=True, null=True, verbose_name='Argumentos'),
        ),
    ]