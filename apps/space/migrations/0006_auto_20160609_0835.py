# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0005_auto_20160609_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='cuenta_bancaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space.TipoCuenta'),
        ),
    ]
