from django.db import models
from django.contrib.auth.models import User
from tipos_recursos.models import Recurso


class Reclamo(models.Model):
    """
    Clase para realizar reclamos acerca de cualquier inquietud con respecto a los recursos
    """
    ESTADOS_RECLAMO_CHOICES = (
        ('NUE', 'NUEVO'),
        ('PEN', 'PENDIENTE'),
        ('ATE', 'ATENDIDO'),
    )

    recurso = models.ForeignKey(Recurso, blank=False, null=False)
    usuario = models.ForeignKey(User, blank=False)
    descripcion = models.TextField(default='', help_text='', blank=False)
    fecha = models.DateField()
    estado = models.CharField(max_length=3, null=False, choices=ESTADOS_RECLAMO_CHOICES, default='NUE')

    class Meta:
        permissions = (
            ("per_crear_reclamo", "Puede crear reclamo"),
            ("per_modificar_reclamo", "Puede modificar estado reclamo"),
            ("per_ver_reclamo", "Puede ver ")
            ("per_ver_reclamo_admin", "Puede ver todos los reclamos")
        )
        db_table = 'reclamos'


