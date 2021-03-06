from tipos_recursos.models import Recurso, TipoRecurso
from django.db import models


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
        return self.codigo

    TIPOS_MANTENIMIENTOS_CHOICE = (
        ('PRE', 'PREVENTIVO'),
        ('COR', 'CORRECTIVO')
    )

    ESTADO_MANTENIMIENTO_CHOICE = (
        ('INI', 'INICIADO'),
        ('FIN', 'FINALIZADO')
    )

    tipo_recurso = models.ForeignKey(TipoRecurso, blank=False)
    recurso = models.ForeignKey(Recurso, null=False)
    motivo = models.TextField(max_length=50, null=False)
    tipo_mantenimiento = models.CharField(max_length=3, null=False, choices=TIPOS_MANTENIMIENTOS_CHOICE, default='PRE')
    fecha_inicio = models.DateField(null=False)
    fecha_fin = models.DateField(blank=True, null=True)
    costo = models.IntegerField(null=False)
    estado = models.CharField(max_length=3, choices=ESTADO_MANTENIMIENTO_CHOICE, default='INI')

    class Meta:
        permissions = (
            ('per_crear_mantenimiento_recurso', 'Puede crear el mantenimiento de un recurso'),
            ('per_modificar_mantenimiento_recurso', 'Puede modificar el mantenimiento de un recurso'),
            ('per_lista_mantenimientos', 'Puede listar todos los mantenimientos del tipo de recurso del que esta encargado')
        )
        db_table = 'mantenimiento'