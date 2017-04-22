from django.db import models


class TipoRecurso(models.Model):
    """
        Clase Tipo de Recurso
    """
    ESTADO_CHOICE = (
        ('A', 'ACTIVO'),
        ('I', 'INACTIVO')
    )
    nombre = models.TextField(primary_key=True, max_length=50)
    descripcion = models.TextField(max_length=50)
    lista_caracteristicas = models.TextField(null=False)
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
        db_table = 'tipos_recursos'


class Estados(models.Model):
    """
        Clase Estados
        Es la clase que se crea para tener los estados del recurso
    """
    codigo = models.CharField(max_length=3, null=False, primary_key=True)
    descripcion = models.TextField(max_length=50, null=False)

    def __str__(self):
        return self.descripcion

    class Meta:
        permissions = (
            ("per_crear_estado", "Puede crear estado de recurso"),
            ("per_eliminar_estado", "Puede eliminar estado de recurso"),
            ("per_ver_estado", "Puede ver estado de recurso"),
            ("per_editar_estado", "Puede editar estado de recurso")
        )
        db_table = 'estados'


class Recurso(models.Model):
    """
        Clase Recurso
        
    """

    def __str__(self):
        return self.tipo_recurso

    ACTIVO_CHOICE = (
        ('A', "ACTIVO"),
        ('I', "INACTIVO")
    )

    codigo_recurso = models.CharField(max_length=10, null=False, primary_key=True)
    nombre_recurso = models.TextField(max_length=50, null=False)
    descripcion_recurso = models.TextField(max_length=50, null=False,)
    tipo_recurso = models.OneToOneField(TipoRecurso, null=False)
    activo = models.CharField(max_length=1, null=False, choices=ACTIVO_CHOICE, default='A')

    class Meta:
        permissions = (
            ("per_crear_recurso", "Puede crear recurso"),
            ("per_eliminar_recurso", "Puede eliminar recurso"),
            ("per_ver_recurso", "Puede ver recurso"),
            ("per_editar_recurso", "Puede editar recurso")
        )

        db_table = 'recursos'