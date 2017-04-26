# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-24 22:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('codigo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=50)),
            ],
            options={
                'permissions': (('per_crear_estado', 'Puede crear estado de recurso'), ('per_eliminar_estado', 'Puede eliminar estado de recurso'), ('per_ver_estado', 'Puede ver estado de recurso'), ('per_editar_estado', 'Puede editar estado de recurso')),
                'db_table': 'estados',
            },
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('codigo_recurso', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_recurso', models.TextField(max_length=50)),
                ('descripcion_recurso', models.TextField(max_length=50)),
                ('activo', models.CharField(choices=[('A', 'ACTIVO'), ('I', 'INACTIVO')], default='A', max_length=1)),
            ],
            options={
                'permissions': (('per_crear_recurso', 'Puede crear recurso'), ('per_eliminar_recurso', 'Puede eliminar recurso'), ('per_ver_recurso', 'Puede ver recurso'), ('per_editar_recurso', 'Puede editar recurso')),
                'db_table': 'recursos',
            },
        ),
        migrations.CreateModel(
            name='TipoRecurso',
            fields=[
                ('nombre', models.TextField(max_length=50, primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=50)),
                ('lista_caracteristicas', models.TextField()),
                ('estado', models.CharField(choices=[('A', 'ACTIVO'), ('I', 'INACTIVO')], default='A', max_length=1)),
            ],
            options={
                'permissions': (('per_crear_tiporecurso', 'Puede crear tipo recurso'), ('per_eliminar_tiporecurso', 'Puede eliminar tipo recurso'), ('per_ver_tiporecurso', 'Puede ver tipo recurso'), ('per_editar_tiporecurso', 'Puede editar tipo recurso')),
                'db_table': 'tipos_recursos',
            },
        ),
        migrations.AddField(
            model_name='recurso',
            name='tipo_recurso',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tipos_recursos.TipoRecurso'),
        ),
    ]
