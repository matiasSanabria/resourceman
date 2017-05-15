from django.contrib.auth.decorators import login_required
from ..tipos_recursos.models import Recurso
from django.db import models


@login_required
class Mantenimiento(models.Model):
    """
    Model que define un mantenimiento de recurso
    *Campos*
    
    1. codigo: codigo del mantenimiento e identificador primario
    #. recurso: id del recurso que esta en mantenimiento
    #. motivo: descripcio por la  que el recurso esta en mantenimiento
    #. tipo_mantenimiento: si es mantenimiento correctivo o preventivo
    #. fecha_inicio: fecha de inicio del mantenimiento
    #. fecha_fin: fecha de finalizacion del mantenimiento
    #. mantenimiento_programado: fecha del siguiente mantenimiento
    #. costo: cuanto es el costo del mantenimiento
    """
    def __str__(self):
        return self.recurso


    TIPOS_MANTENIMIENTOS_CHOICE = (
        ('PRE', 'PREVENTIVO'),
        ('COR', 'CORRECTIVO')
    )

    codigo = models.AutoField(primary_key=True)
    recurso = models.OneToOneField(Recurso, null=False)
    motivo = models.TextField(max_length=50, null=False)
    tipo_mantenimiento = models.CharField(max_length=3, null=False, choices=TIPOS_MANTENIMIENTOS_CHOICE, default='PRE')
    fecha_inicio = models.DateField(null=False)
    fecha_fin = models.DateField(blank=True, null=True)
    mantenimiento_programado = models.DateField(null=False)
    costo = models.IntegerField(null=False)

    class Meta:
        permissions = (
            ('per_crear_mantenimiento_recurso', 'Puede crear el mantenimiento de un recurso'),
            ('per_modificar_mantenimiento_recurso', 'Puede modificar el mantenimiento de un recurso'),
        )
        db_table = 'mantenimiento'