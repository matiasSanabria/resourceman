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


class SolicitudReservas(models.Model):
    ESTADO_SOLICITUD = (
        ('CO', "CONCLUIDA"),
        ('PP', "POR PROCESAR"),
        ('CA', "CANCELADA"),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_recurso = models.ForeignKey(TipoRecurso, blank=True)
    recurso = models.ForeignKey(Recurso, blank=True)
    fecha_solicitud = models.DateTimeField(null=False)
    fecha_reserva = models.DateField(blank=True, null=False)
    hora_ini = models.TimeField(blank=True, null=False)
    hora_fin = models.TimeField(blank=True, null=False)
    descripcion = models.CharField(max_length=70, blank=True, null=False)
    estado = models.CharField(max_length=2, null=False, choices=ESTADO_SOLICITUD, default='RE')

    class Meta:
        permissions = (
            ('per_solicitar_reserva', "Puede solicitar reservar"),
            ('per_cancelar_solicitud_reserva', "Puede cancelar la solicitud de reserva reserva"),
            ('per_listar_sus_solicitudes_reservas', "Puede ver sus solicitudes de reservas"),#desde el user
            ('per_listar_solicitudes_reservas', "Puede listar las solicitudes de reservas"),#desde el admin
        )
        db_table = 'solicitud_reservas'
