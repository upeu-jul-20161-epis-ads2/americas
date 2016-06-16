# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 13:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0004_tipocuenta_numero_cuenta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space.TipoCuenta')),
            ],
            options={
                'verbose_name': 'Cuenta',
                'verbose_name_plural': 'Cuentas',
            },
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='cuenta_bancaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space.Cuenta'),
        ),
    ]