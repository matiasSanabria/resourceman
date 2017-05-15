from django.db import models

# Create your models here.
from django.utils import timezone

# from resourceman.resourceman.tipos_recursos.models import Recurso, TipoRecurso
from ..tipos_recursos.models import Recurso, TipoRecurso
from django.contrib.auth.models import User
from django import forms


class Reservas(models.Model):
    ESTADO_RESERVA = (
        ('RE', "REALIZADA"),
        ('CA', "CANCELADA"),
        ('RA', "REASIGNADA"),
        ('EC', "EN CURSO"),
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