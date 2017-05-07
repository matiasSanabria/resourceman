from django.db import models
from django.contrib.auth.models import Group, GroupManager

"""
    Utilizacion del modelo Group de Django para el manejo de roles.

    *Campos de Group*

    1. ``id``: Codificacion del Rol.
    #. ``name``: Descripcion del Rol.

    *Campos de Group_Permissions:*
    1. ``id``: Codificacion de la referencia Rol-Permiso.
    #. ``group_id``: Id del Rol a relacionar.
    #. ``permission_id``: Id Permisos relacionados al Rol.

    Returns
    -------
    model: ``django.contrib.auth.models``
        Un model propio heredado de django.contrib.auth.models .

"""
# Create your models here.
