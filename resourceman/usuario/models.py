# from django.contrib.auth.models import User, Group
# from django.db import models
#
#
# # Create your models here.
# class Usuario(models.Model):
#     PRIORITY_CHOICES = (
#         ('ADM', "ADMINISTRADOR DE RECURSOS"),
#         ('TIT', "PROFESOR TITULAR"),
#         ('ADJ', "PROFESOR ADJUNTO"),
#         ('ASI', "PROFESOR ASISTENTE"),
#         ('ENC', "ENCARGADO DE CATEDRA"),
#         ('AUX', "AUXILIAR DE ENSENHANZA"),
#         ('ALU', "ALUMNO"),
#         ('FUN', "FUNCIONARIO"),
#         ('NON', "NO-CATEGORIZADO"),
#     )
#
#     usuario = models.OneToOneField(User, on_delete=models.CASCADE)
#     nro_documento = models.TextField(blank=False, max_length=20, null=False)
#     direccion = models.TextField(max_length=100, blank=True, null=True)
#     telefono = models.TextField(max_length=20, blank=True, null=True)
#     prioridad = models.CharField(max_length=3, choices=PRIORITY_CHOICES, default='NON', null=False, blank=False)
#     rol = models.OneToOneField(Group, on_delete=models.CASCADE)
#
#     class Meta:
#         permissions = (
#             ('per_crear_usuario', "Puede crear usuario"),
#             ('per_editar_usuario', "Puede editar usuario"),
#             ('per_eliminar_usuario', "Puede eliminar usuario"),
#             ('per_ver_usuario', "Puede ver usuario"),
#         )