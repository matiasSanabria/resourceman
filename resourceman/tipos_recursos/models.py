from django.db import models


# Create your models here.
class TipoRecurso(models.Model):
    ESTADO_CHOICE = (
        ('A', 'ACTIVO'),
        ('I', 'INACTIVO')
    )
    nombre = models.TextField(primary_key=True, max_length=50)
    descripcion = models.TextField(max_length=50)
    lista_caracteristicas = models.TextField()
    estado = models.CharField(max_length=1, null=False, blank=False, choices=ESTADO_CHOICE, default='A')

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = (
            ("per_crear_tiporecurso", "Puede crear tipo recurso"),
            ("per_eliminar_tiporecurso", "Puede eliminar tipo recurso"),
            ("per_ver_tiporecurso", "Puede ver tipo recurso"),
            ("per_editar_tiporecurso", "Puede editar tipo recurso")
        )