from django.db import models

# Create your models here.


class Recurso(models.Model):
    ESTADO_CHOICE = (
        ('DIS', "DISPONIBLE"),
        ('SOL', "SOLICITADO"),
        ('RES', "RESERVADO"),
        ('MAN', "EN MANTENIMIENTO"),
        ('USO', "EN USO"),
        ('NDE', "NO DEVUELTO"),
        ('FUS', "FUERA DE USO"),
    )

    id = models.AutoField(primary_key=True)
    codigo_recurso = models.TextField(max_length=20, unique=True, blank=False)
    descripcion_recurso = models.TextField(max_length=50, blank=True)
    #tipo_recurso = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE, limit_choices_to={'estado':'A'})
    estado_recurso = models.CharField(max_length=3, choices=ESTADO_CHOICE, default='DIS', blank=False, null=False)

    class Meta:
        permissions = (
            ("per_crear_recurso", "Puede crear recurso"),
            ("per_eliminar_recurso", "Puede eliminar recurso"),
            ("per_ver_recurso", "Puede ver recurso"),
            ("per_editar_recurso", "Puede editar recurso")
        )