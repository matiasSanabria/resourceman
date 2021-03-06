from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from reservas.models import SolicitudReservas, Reservas
from usuarios.models import Usuario
from tipos_recursos.models import Estados, Recurso
from reservas.forms import ReservasForm, SolicitudForm
from datetime import date, timedelta
from django.core.mail import send_mail
from django.conf import settings


class Command(BaseCommand):

    def reservarSolicitud(self, pk):
        # controlar si el recurso no esta fuera de uso o en mantenimiento
        solicitud = SolicitudReservas.objects.get(id=pk)
        mantenimiento = Estados.objects.get(descripcion = "EN MANTENIMIENTO")
        fueradeuso = Estados.objects.get(descripcion = "FUERA DE USO")
        recurso = Recurso.objects.get(codigo_recurso = solicitud.recurso.codigo_recurso)
        if (recurso.estado != mantenimiento and recurso.estado != fueradeuso):
            reservasss = Reservas.objects.filter(recurso=recurso).filter(fecha=solicitud.fecha_reserva).filter(hora_ini=solicitud.hora_ini).filter(hora_fin=solicitud.hora_fin).exclude(estado='TE').exclude(estado='CA')
            editar = True
            for recu in reservasss :
                if recu.recurso == recurso:
                    editar=False
            if editar:
                reserva2 = ReservasForm()
                reserva = reserva2.save(commit=False)
                reserva.tipo_recurso = solicitud.tipo_recurso
                reserva.recurso = solicitud.recurso
                reserva.usuario = solicitud.usuario
                reserva.estado = 'RE'
                reserva.descripcion = solicitud.descripcion
                reserva.fecha = solicitud.fecha_reserva
                reserva.hora_ini = solicitud.hora_ini
                reserva.hora_fin = solicitud.hora_fin
                reserva.save()

        if recurso.estado == mantenimiento:
            user = User.objects.get(id=solicitud.usuario.id)
            mensaje = 'Hola ' + user.first_name + ' le informamos que el recurso que solicito: ' + solicitud.recurso.nombre_recurso + ' se encuentra en mantenimiento.\n' + '\nFecha:  ' + solicitud.fecha_reserva.strftime(
                '%d/%m/%Y') + '\nDesde las: ' + solicitud.hora_ini.strftime('%H:%M') + ' hasta las ' + solicitud.hora_fin.strftime(
                '%H:%M') + '\nPor favor pongase en contanto con el administrador para mas informacion.'
            try:
                send_mail('Reserva', mensaje, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
            except Exception:
                pass

    def resolverSolicitudes(self):
        fecha = date.today() + timedelta(days=2)
        solicitudes = SolicitudReservas.objects.filter(fecha_reserva=fecha).filter(estado='PP').order_by('hora_ini')
        if solicitudes:
            # ayuda para recorrido y encontrado
            listaSolicitudes = []
            for solicitud in solicitudes:
                listaSolicitudes.append(solicitud)
            while listaSolicitudes:
                # encontrar el mayor
                mayorRango = listaSolicitudes[0]
                usuarioMayor = Usuario.objects.get(usuario=mayorRango.usuario)
                for solicitud in listaSolicitudes:
                    usuarioSolicitante = Usuario.objects.get(usuario=solicitud.usuario)
                    if usuarioSolicitante.prioridad.prioridad > usuarioMayor.prioridad.prioridad:
                        mayorRango = solicitud
                    elif usuarioSolicitante.prioridad.prioridad == usuarioMayor.prioridad.prioridad:
                        if solicitud.fecha_solicitud < mayorRango.fecha_solicitud:
                            mayorRango = solicitud
                listaSolicitudes.remove(mayorRango)
                # ver conflictos y solucionarlos
                for solicitud in listaSolicitudes:
                    if solicitud.hora_fin < mayorRango.hora_fin and solicitud.hora_fin > mayorRango.hora_ini:
                        solicitud.estado = 'CO'
                        solicitud.save()
                        listaSolicitudes.remove(solicitud)
                    elif solicitud.hora_ini < mayorRango.hora_fin and solicitud.hora_ini > mayorRango.hora_ini:
                        solicitud.estado = 'CO'
                        solicitud.save()
                        listaSolicitudes.remove(solicitud)
                    elif solicitud.hora_ini < mayorRango.hora_ini and solicitud.hora_fin > mayorRango.hora_fin:
                        solicitud.estado = 'CO'
                        solicitud.save()
                        listaSolicitudes.remove(solicitud)
                    elif solicitud.hora_ini == mayorRango.hora_ini and solicitud.hora_fin == mayorRango.hora_fin:
                        solicitud.estado = 'CO'
                        solicitud.save()
                        listaSolicitudes.remove(solicitud)
                mayorRango.estado = 'CO'
                mayorRango.save()
                self.reservarSolicitud(mayorRango.id)

    def handle(self, *args, **options):
        self.resolverSolicitudes()

