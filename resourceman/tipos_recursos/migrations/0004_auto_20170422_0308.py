# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 03:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tipos_recursos', '0003_estados_recurso'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='estados',
            table='estados',
        ),
        migrations.AlterModelTable(
            name='recurso',
            table='recursos',
        ),
        migrations.AlterModelTable(
            name='tiporecurso',
            table='tipos_recursos',
        ),
    ]
