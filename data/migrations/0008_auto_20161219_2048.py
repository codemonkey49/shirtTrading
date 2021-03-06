# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-19 20:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sentBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messageFrom', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='sentTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messageTo', to=settings.AUTH_USER_MODEL),
        ),
    ]
