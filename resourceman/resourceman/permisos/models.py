from django.db import models
from django.contrib.auth.models import Permission
"""
    Utilizacion del modelo Permission para el manejo de permisos.

     de Django, mediante una relación de 1-1.

    *Campos de Permission:*

    1. ``codename``: Codificacion del nombre.
    #. ``name``: Descripcion del permiso.
    #. ``content_type``: Referencia a apliccion de acceso

    *Campos de Content_Type*

    1. ``id``: Codificacion de Content_type.
    #. ``app_label``: Referencia a aplicacion.
    #. ``model``: Acceso a modelos.

    Returns
    -------
    model: ``django.contrib.auth.models``
        Un model propio heredado de django.contrib.auth.models .

    """
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)

# def guardar(app_label, model):
#     p = AuthPermission()
#     p.content_type.app_label = app_label
#     p.content_type.model = model
#     p.save()

# class Roles (models.Model):
#     Meta:
#         models = Gr
