# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatUpdateRouter',
            fields=[
                ('chatupdate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chat.ChatUpdate')),
            ],
            options={
                'managed': False,
            },
            bases=('chat.chatupdate',),
        ),
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='is_running',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ChatContextRouter',
            fields=[
                ('context_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chat.Context')),
            ],
            options={
                'managed': False,
            },
            bases=('chat.context',),
        ),
        migrations.AddField(
            model_name='context',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Chat'),
        ),
    ]
