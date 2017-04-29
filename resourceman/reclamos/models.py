from django.db import models
from django.contrib.auth.models import User


class Reclamo(models.Model):
    # recurso = models.ForeignKey(
    #     Recurso,
    #     blank=True,
    #     # limit_choices_to={'codename__startswith':'sar_'}
    # )
    recurso = models.TextField(default='', help_text='', blank=False)
    usuario = models.ForeignKey(
        User,
        blank=False,
    )
    descripcion = models.TextField(default='', help_text='', blank=False)
    fecha = models.DateField()
    # aqui se definen los campos
    # hora = models.TimeField()
