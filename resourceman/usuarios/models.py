from django.contrib.auth.models import User, Group
from django.db import models


class PrioridadUsuario(models.Model):
    def __str__(self):
        return self.descripcion

    codigo = models.TextField(blank=False, max_length=4, null=False, unique=True)
    descripcion = models.TextField(blank=False, max_length=50, null=False, unique=True)
class Usuario(models.Model):

    # PRIORITY_CHOICES = (
    #     ('ADM', "ADMINISTRADOR DE RECURSOS"),
    #     ('TIT', "PROFESOR TITULAR"),
    #     ('ADJ', "PROFESOR ADJUNTO"),
    #     ('ASI', "PROFESOR ASISTENTE"),
    #     ('ENC', "ENCARGADO DE CATEDRA"),
    #     ('AUX', "AUXILIAR DE ENSENHANZA"),
    #     ('ALU', "ALUMNO"),
    #     ('FUN', "FUNCIONARIO"),
    #     ('NON', "NO-CATEGORIZADO"),
    # )

    # id = models.AutoField(null=False, primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nro_documento = models.TextField(blank=False, max_length=20, null=False, unique=True)
    direccion = models.TextField(max_length=100, blank=True, null=True)
    telefono = models.TextField(max_length=20, blank=True, null=True)
    # prioridad = models.CharField(max_length=3, choices=PRIORITY_CHOICES, default='NON', null=False, blank=False)
    prioridad = models.ForeignKey(PrioridadUsuario)
    # rol = models.OneToOneField(Group, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ('per_crear_usuario', "Puede crear usuario"),
            ('per_editar_usuario', "Puede editar usuario"),
            ('per_eliminar_usuario', "Puede eliminar usuario"),
            ('per_ver_usuario', "Puede ver usuario"),
        )
