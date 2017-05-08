from django.db import models
from django.contrib.auth.models import User
from ..tipos_recursos.models import Recurso


class EstadoReclamo(models.Model):
    """
        Definicion del model para los Estados de los reclamos

        *Campos:*

        1. ``codigo``: nombre del estado del reclamo utilizado como clave primaria
        #. ``descripcion``: descripcion del estado del reclamo

        Returns
        -------
        model: ``django.db.models.Model``
            Un model propio heredado de django.db.models.Model con los campos adicionales.

        """
    codigo = models.CharField(max_length=3, null=False, primary_key=True)
    descripcion = models.TextField(max_length=50, null=False)

    def __str__(self):
        return self.descripcion

    class Meta:
        permissions = (
            ("per_crear_estado_reclamo", "Puede crear estado de reclamo"),
            ("per_editar_estado_reclamo", "Puede editar estado de reclamo")
        )
        db_table = 'estado_reclamo'


class Reclamo(models.Model):
    """
    Clase para realizar reclamos acerca de cualquier inquietud con respecto a los recursos
    """
    recurso = models.ForeignKey(Recurso, blank=False, null=False)
    usuario = models.ForeignKey(User, blank=False)
    descripcion = models.TextField(default='', help_text='', blank=False)
    fecha = models.DateField()
    estado = models.OneToOneField(EstadoReclamo, max_length=3, null=False)

    class Meta:
        permissions = (
            ("per_crear_reclamo", "Puede crear reclamo"),
            ("per_modificar_reclamo", "Puede modificar estado reclamo"),
            ("per_ver_reclamo", "Puede ver ")
        )
        db_table = 'reclamos'


