from django.contrib.auth.models import User, Group, Permission
from django.db import models

"""
Utilizacion del modelo User de Django para el manejo de usuarios.

*Campos de User*

1. ``id``: Codificacion del Usuario.
#. ``password``: Contraseña del usuario.
#. ``last_login``: Ultimo acceso del usuario.
#. ``is_superuser``: Deficion de superusuario.
#. ``username``: Username para el inicio de sesion.
#. ``first_name``: Nombre del usuario.
#. ``last_name``: Apellido del usuario.
#. ``email``: Email del usuario.
#. ``is_staff``: Es personal.
#. ``is_active``: El usuario existe dentro del sistema.
#. ``date_joined``: Fecha de registro.

"""


class PrioridadUsuario(models.Model):
    """
    Un model de definicion de prioridades para model Usuario.

    Se asocia al model Usuario, mediante una relación de 1-1.

    *Campos:*

    1. ``id``: Identificador de la prioridad.
    #. ``codigo``: Codigo alfabetico referenciado a la prioridad.
    #. ``descipcion``: Describe la prioidad.
    """
    def __str__(self):
        return self.descripcion

    codigo = models.TextField(blank=False, max_length=4, null=False, unique=True)
    descripcion = models.TextField(blank=False, max_length=50, null=False, unique=True)
    prioridad = models.IntegerField(blank=False)
    class Meta:
        permissions = (
            ('per_crear_prioridad', "Puede crear Prioridad"),
            ('per_editar_prioridad', "Puede editar Piroridad"),
            ('per_eliminar_prioridad', "Puede eliminar Prioridad"),
            ('per_listar_prioridad', "Puede eliminar Prioridad"),
        )
        db_table = 'prioridad_usuario'


class Usuario(models.Model):
    """
    Un model con campos adicionales para model User.

    Asocia más campos al model user de Django, mediante una relación de 1-1.

    *Campos adicionales:*

    1. ``usuario``: Referencia al model User de Django.
    #. ``nro_documento``: Cédula de identidad u otro número de identidad del usuario.
    #. ``direccion``: Domicilio del usuario.
    #. ``telefono``: Número de teléfono del usuario.
    #. ``prioridad``: referencia al model prioridad de usuarios.

    """

    # id = models.AutoField(null=False, primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nro_documento = models.TextField(blank=False, max_length=20, null=False, unique=True)
    direccion = models.TextField(max_length=100, blank=True, null=True)
    telefono = models.TextField(max_length=20, blank=True, null=True)
    # prioridad = models.CharField(max_length=3, choices=PRIORITY_CHOICES, default='NON', null=False, blank=False)
    prioridad = models.ForeignKey(PrioridadUsuario)
    # rol = models.OneToOneField(Group, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ('per_crear_usuario', "Puede crear usuario"),
            ('per_editar_usuario', "Puede editar usuario"),
            ('per_eliminar_usuario', "Puede eliminar usuario"),
            ('per_listar_usuario', "Puede ver usuario"),
        )
        db_table = 'usuario'
