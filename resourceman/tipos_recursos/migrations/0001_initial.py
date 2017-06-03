# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-30 19:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaracteristicasRecursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.TextField()),
                ('valor', models.TextField()),
            ],
            options={
                'db_table': 'caracteristicas_recurso',
            },
        ),
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('codigo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=50)),
            ],
            options={
                'permissions': (('per_crear_estado', 'Puede crear estado de recurso'), ('per_eliminar_estado', 'Puede eliminar estado de recurso'), ('per_listar_estados', 'Puede listar estados de los recursos'), ('per_editar_estado', 'Puede editar estado de recurso')),
                'db_table': 'estados',
            },
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('codigo_recurso', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_recurso', models.TextField(max_length=50)),
                ('activo', models.CharField(choices=[('A', 'ACTIVO'), ('I', 'INACTIVO')], default='A', max_length=1)),
                ('mantenimiento_programado', models.DateField(blank=True, default=datetime.date.today, max_length=10, null=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipos_recursos.Estados')),
            ],
            options={
                'permissions': (('per_crear_recurso', 'Puede crear recurso'), ('per_eliminar_recurso', 'Puede eliminar recurso'), ('per_listar_recursos', 'Puede listar recursos'), ('per_editar_recurso', 'Puede editar recurso')),
                'db_table': 'recursos',
            },
        ),
        migrations.CreateModel(
            name='TipoRecurso',
            fields=[
                ('nombre', models.TextField(max_length=50, primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=50)),
                ('lista_caracteristicas', models.TextField(default='{"clave":"ejemplo", "valor":"ejemplo"},\n{"clave":"ejemplo", "valor":"ejemplo"}')),
                ('estado', models.CharField(choices=[('A', 'ACTIVO'), ('I', 'INACTIVO')], default='A', max_length=1)),
            ],
            options={
                'permissions': (('per_crear_tiporecurso', 'Puede crear tipo recurso'), ('per_eliminar_tiporecurso', 'Puede eliminar tipo recurso'), ('per_listar_tiporecurso', 'Puede listar los tipos recursos'), ('per_editar_tiporecurso', 'Puede editar tipo recurso')),
                'db_table': 'tipos_recursos',
            },
        ),
        migrations.AddField(
            model_name='recurso',
            name='tipo_recurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipos_recursos.TipoRecurso'),
        ),
        migrations.AddField(
            model_name='caracteristicasrecursos',
            name='codigo_recurso',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tipos_recursos.Recurso'),
        ),
        migrations.AddField(
            model_name='caracteristicasrecursos',
            name='codigo_tipo_recurso',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tipos_recursos.TipoRecurso'),
        ),
        migrations.AlterUniqueTogether(
            name='caracteristicasrecursos',
            unique_together=set([('codigo_recurso', 'codigo_tipo_recurso')]),
        ),
    ]
