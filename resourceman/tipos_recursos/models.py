from django.db import models
from django.contrib.auth.models import User, Permission


class TipoRecurso(models.Model):
    """
    Definicion del model para los Tipos de Recursos

    *Campos:*

    1. ``nombre``: nombre del tipo de recurso utilizado como clave primaria
    #. ``descripcion``: descripcion del tipo de recurso
    #. ``lista_caracteristicas``: lista de las caracteristicas que tiene el tipo de recurso
    #. ``estado``: indica si el tipo de recurso esta activo o inactivo

    Returns
    -------
    model: ``django.db.models.Model``
        Un model propio heredado de django.db.models.Model con los campos adicionales.

    """

    ESTADO_CHOICE = (
        ('A', 'ACTIVO'),
        ('I', 'INACTIVO')
    )
    nombre = models.TextField(primary_key=True, max_length=50)
    descripcion = models.TextField(max_length=50)
    lista_caracteristicas = models.TextField(null=False, default="{{\"clave\":\"ejemplo\", \"valor\":\"ejemplo\"},\n{\"clave\":\"ejemplo\", \"valor\":\"ejemplo\"}}")
    estado = models.CharField(max_length=1, null=False, blank=False, choices=ESTADO_CHOICE, default='A')

    def __str__(self):
        return self.nombre

    def obtener_caracteristicas(self, nombre):
        list = TipoRecurso.objects.get(nombre=nombre)
        list = list.lista_caracteristicas
        list = list[2:(len(list)-2)]
        list = list.split(',')

        caracteristica = []
        tipo_dato = []

        for item in list:
            caracteristica.append(item[0])
            tipo_dato.append(item[1])

        caracteristicas = [caracteristica, tipo_dato]

        return caracteristicas




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
    Definicion del model para los Estados de los recursos

    *Campos:*

    1. ``codigo``: nombre del estado del recurso utilizado como clave primaria
    #. ``descripcion``: descripcion del estado del recurso

    Returns
    -------
    model: ``django.db.models.Model``
        Un model propio heredado de django.db.models.Model con los campos adicionales.

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
    Definicion del model para los Estados de los recursos

    *Campos:*

    1. ``codigo_recurso``: codigo del recurso recurso utilizado como clave primaria
    #. ``nombre_recurso``: nombre del recurso
    #. ``descripcion_recurso``: descripcion del estado del recurso
    #. ``tipo_recurso``: tipo de recurso del que hereda sus caracteristicas
    #. ``activo``: indica si el recurso esta activo o no

    Returns
    -------
    model: ``django.db.models.Model``
        Un model propio heredado de django.db.models.Model con los campos adicionales.
    """

    def __str__(self):
        return self.nombre_recurso

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


def per_num():
    per = Permission.objects.get(codename='per_crear_recurso')
    return per.id

class Encargado(models.Model):
    tipo_recurso = models.OneToOneField(TipoRecurso, on_delete=models.CASCADE)
    usuario = models.ForeignKey(
        User,
        blank=True,
        limit_choices_to={'groups__permissions': per_num()}
    )

    class Meta:

        db_table = 'encargado_recurso'