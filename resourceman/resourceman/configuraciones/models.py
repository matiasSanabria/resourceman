from django.db import models


class RegistroUsuario(models.Model):
    """
    Clase para la plantilla de envio de notificaciones de registro de usuario
    
    *Campos:*
    
    1. ``id``: id del registro de usuario utilizado como clave primaria
    #. ``asunto``: asunto con el que sera enviado el correo
    #. ``mensaje``: mensaje del cuerpo del correo    
    """
    def __str__(self):
        return self.id

    id = models.AutoField(primary_key=True)
    asunto = models.TextField(max_length=30, blank=False, null=False)
    mensaje = models.TextField(max_length=100, blank=False, null=False)

    class Meta:
        permissions = (
            ("per_configuracion_registro_usuario", "Puede ver la plantilla para el envio de notificaciones de registro de usuario"),
        )
        db_table = 'registro_usuario'
