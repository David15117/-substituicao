# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamentosocitacao',
            name='funcionario',
            field=models.ManyToManyField(to='transporte.Funcionario'),
        ),
    ]
