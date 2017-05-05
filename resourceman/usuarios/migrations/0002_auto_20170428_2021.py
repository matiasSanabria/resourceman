# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-28 20:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prioridadusuario',
            options={'permissions': (('per_crear_prioridad', 'Puede crear Prioridad'), ('per_editar_prioridad', 'Puede editar Piroridad'), ('per_eliminar_prioridad', 'Puede eliminar Prioridad'), ('per_listar_prioridad', 'Puede eliminar Prioridad'))},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'permissions': (('per_crear_usuario', 'Puede crear usuario'), ('per_editar_usuario', 'Puede editar usuario'), ('per_eliminar_usuario', 'Puede eliminar usuario'), ('per_listar_usuario', 'Puede ver usuario'))},
        ),
    ]