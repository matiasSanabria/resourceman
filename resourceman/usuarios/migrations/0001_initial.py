# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-30 19:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PrioridadUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.TextField(max_length=4, unique=True)),
                ('descripcion', models.TextField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'prioridad_usuario',
                'permissions': (('per_crear_prioridad', 'Puede crear Prioridad'), ('per_editar_prioridad', 'Puede editar Piroridad'), ('per_eliminar_prioridad', 'Puede eliminar Prioridad'), ('per_listar_prioridad', 'Puede eliminar Prioridad')),
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_documento', models.TextField(max_length=20, unique=True)),
                ('direccion', models.TextField(blank=True, max_length=100, null=True)),
                ('telefono', models.TextField(blank=True, max_length=20, null=True)),
                ('prioridad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.PrioridadUsuario')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'usuario',
                'permissions': (('per_crear_usuario', 'Puede crear usuario'), ('per_editar_usuario', 'Puede editar usuario'), ('per_eliminar_usuario', 'Puede eliminar usuario'), ('per_listar_usuario', 'Puede ver usuario')),
            },
        ),
    ]
