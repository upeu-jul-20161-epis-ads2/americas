# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('params', '0005_socio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socio',
            name='socio',
        ),
        migrations.AddField(
            model_name='socio',
            name='persona',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='params.Person'),
            preserve_default=False,
        ),
    ]
