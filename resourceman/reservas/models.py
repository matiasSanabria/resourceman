from django.db import models

# Create your models here.

from tipos_recursos.models import Recurso, TipoRecurso
from django.contrib.auth.models import User


class Reservas(models.Model):
    """
    Definicion del model para las reservas

    *Campos:*

    1. ``tipo_recurso``: tipo de recurso a reservar
    #. ``recurso``: recurso a reservar
    #. ``fecha``: fecha de reserva
    #. ``hora_ini``: hora de inicio de la reserva
    #. ``hora_fin``: hora de fin de reserva
    #. ``usuario``: usuario que realizo la reserva
    #. ``descripcion``: pequeña descripcion de la reserva
    #. ``estado``: indica el estado en que se encuentra la reserva
    """
    ESTADO_RESERVA = (
        ('RE', "REALIZADA"),
        ('CA', "CANCELADA"),
        ('RA', "REASIGNADA"),
        ('EC', "EN CURSO"),
        ('ND', "NO DEVUELTO"),
        ('TE', "TERMINADA"),
    )
    tipo_recurso = models.ForeignKey(TipoRecurso, blank=True)
    recurso = models.ForeignKey(
        Recurso,
        blank=True,
        limit_choices_to={'estado__descripcion': 'DISPONIBLE'}
    )
    # default = timezone.now
    fecha = models.DateField(blank=True, null=False)
    hora_ini = models.TimeField(blank=True, null=False)
    hora_fin = models.TimeField(blank=True, null=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=70, blank=True, null=False)
    estado = models.CharField(max_length=2, null=False, choices=ESTADO_RESERVA, default='RE')

    class Meta:
        permissions = (
            ('per_realizar_reserva', "Puede reservar"),
            ('per_cancelar_reserva', "Puede cancelar la reserva"),
            ('per_listar_sus_reservas', "Puede ver sus reservas"),#desde el user
            ('per_listar_reservas', "Puede listar las reservas"),#desde el admin
        )
        db_table = 'reservas'