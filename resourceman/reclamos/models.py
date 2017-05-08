from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Reclamo(models.Model):
    # recurso = models.ForeignKey(
    #     Recurso,
    #     blank=True,
    #     # limit_choices_to={'codename__startswith':'sar_'}
    # )
    recurso = models.TextField(default='', help_text='', blank=False)
    usuario = models.ForeignKey(User)
    descripcion = models.TextField(default='', help_text='', blank=False)
    fecha = models.DateField()
    # aqui se definen los campos
    # hora = models.TimeField()
    ESTADO_CHOICE = (
        ('N', "NUEVO"),
        ('P', "PENDIENTE"),
        ('A', "ATENDIDO")
    )
    estado = models.CharField(max_length=1, null=False, choices=ESTADO_CHOICE, default='N')

    class Meta:
        permissions = (
            ("per_crear_reclamo", "Puede crear reclamo"),
            ("per_modificar_reclamo", "Puede modificar estado reclamo"),
            ("per_ver_reclamo", "Puede ver ")
        )
        db_table = 'reclamos'

