# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('params', '0003_auto_20160608_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='cell_phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Cell phone'),
        ),
        migrations.AddField(
            model_name='person',
            name='domicile',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Domicile'),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default=0, max_length=50, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('SG', 'Seleccione genero'), ('H', 'Hombre'), ('M', 'Mujer')], default='SG', max_length=50, verbose_name='gender'),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(default=0, max_length=50, verbose_name='First name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='identity_num',
            field=models.CharField(error_messages={'unique': 'eeeee ee'}, max_length=20, verbose_name='Identity num'),
        ),
        migrations.AlterField(
            model_name='person',
            name='identity_type',
            field=models.CharField(choices=[('NID', 'D.N.I.'), ('FC', 'CARNE DE EXTRANJERIA'), ('CB', 'PARTIDA DE NACIMIENTO'), ('OTHER', 'OTROS')], default='NID', max_length=10, verbose_name='Identity type'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Last name'),
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([('identity_type', 'identity_num'), ('first_name', 'last_name', 'domicile', 'phone', 'cell_phone', 'email', 'gender', 'identity_type', 'identity_num')]),
        ),
    ]
