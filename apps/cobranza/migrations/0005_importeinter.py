# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobranza', '0004_auto_20160609_0211'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImporteInter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name_plural': 'ImporteInters',
                'verbose_name': 'ImporteInter',
            },
        ),
    ]
