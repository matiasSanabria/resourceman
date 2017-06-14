from django.test import TestCase
from django.contrib.auth.models import User
from .models import Reservas, SolicitudReservas
from tipos_recursos.models import TipoRecurso, Recurso, Estados
import datetime


class ReservasDiariasTestCase(TestCase):
    def setUp(self):
        print("Iniciando test de reservas diarias")
        tipo_recurso = TipoRecurso.objects.create(
            nombre="AUL",
            descripcion="AULA",
            lista_caracteristicas='{"cantidad_sillas": "varchar2(10)"}, {"cantidad_aires": "varchar2(10)"}',
            estado='A'
        )
        print("tipo de recurso creado: " + tipo_recurso.descripcion)

        estado_recurso = Estados.objects.create(
            codigo="DIS",
            descripcion="DISPONIBLE"
        )
        print("estado de recurso creado: " + estado_recurso.descripcion)

        recurso = Recurso.objects.create(
            codigo_recurso="P1",
            nombre_recurso="Proyector 1",
            tipo_recurso=tipo_recurso,
            estado=estado_recurso
        )
        print("recurso creado: " + recurso.nombre_recurso)

        usuario = User.objects.create(
            username="test",
            email="test@test.com",
            password="test"
        )
        print("usuario creado: " + usuario.username)

        reserva = Reservas.objects.create(
            tipo_recurso=tipo_recurso,
            recurso=recurso,
            fecha=datetime.date.today(),
            hora_ini='08:00',
            hora_fin='09:00',
            descripcion='Test de reserva diaria',
            estado='RE',
            usuario=usuario
        )

        print("reserva creada: " + reserva.tipo_recurso.descripcion + '\n'
                                 + reserva.recurso.codigo_recurso + '\n'
                                 + reserva.fecha.__str__() + '\n'
                                 + reserva.hora_ini + '\n'
                                 + reserva.hora_fin + '\n'
                                 + reserva.descripcion + '\n'
                                 + reserva.estado + '\n'
                                 + reserva.usuario.username)

    def testReservaDiaria(self):
        reserva = Reservas.objects.get(tipo_recurso='AUL')
        self.assertIsNotNone(reserva)
        print("estado actual de la reserva: " + reserva.estado)
        reserva.estado = 'TE'
        reserva.save()

        reserva = Reservas.objects.get(tipo_recurso='AUL')
        print("nuevo estado de la reserva: " + reserva.estado)


class SolicitudReservasTestCase(TestCase):
    def setUp(self):
        print("Iniciando test de solicitu de reservas")
        tipo_recurso = TipoRecurso.objects.create(
            nombre="AUL",
            descripcion="AULA",
            lista_caracteristicas='{"cantidad_sillas": "varchar2(10)"}, {"cantidad_aires": "varchar2(10)"}',
            estado='A'
        )
        print("tipo de recurso creado: " + tipo_recurso.descripcion)

        estado_recurso = Estados.objects.create(
            codigo="DIS",
            descripcion="DISPONIBLE"
        )
        print("estado de recurso creado: " + estado_recurso.descripcion)

        recurso = Recurso.objects.create(
            codigo_recurso="P1",
            nombre_recurso="Proyector 1",
            tipo_recurso=tipo_recurso,
            estado=estado_recurso
        )
        print("recurso creado: " + recurso.nombre_recurso)

        usuario = User.objects.create(
            username="test",
            email="test@test.com",
            password="test"
        )
        print("usuario creado: " + usuario.username)

        solicitud = SolicitudReservas.objects.create(
            tipo_recurso=tipo_recurso,
            recurso=recurso,
            fecha_solicitud=datetime.date.today(),
            fecha_reserva=datetime.date.today() + datetime.timedelta(days=2),
            hora_ini='08:00',
            hora_fin='09:00',
            descripcion='Test de solicitud de reservas',
            estado='PP',
            usuario=usuario
        )

        print("solicitud creada: " + solicitud.tipo_recurso.descripcion + '\n'
                                 + solicitud.recurso.nombre_recurso + '\n'
                                 + solicitud.fecha_solicitud.__str__() + '\n'
                                 + solicitud.fecha_reserva.__str__() + '\n'
                                 + solicitud.hora_ini + '\n'
                                 + solicitud.hora_fin + '\n'
                                 + solicitud.descripcion + '\n'
                                 + solicitud.estado + '\n'
                                 + solicitud.usuario.username)

    def testSolicitudReservas(self):
        solicitud = SolicitudReservas.objects.get(tipo_recurso='AUL')
        self.assertIsNotNone(solicitud)
        print("estado actual de la solicitud: " + solicitud.estado)
        solicitud.estado = 'TE'
        solicitud.save()

        solicitud = SolicitudReservas.objects.get(tipo_recurso='AUL')
        print("nuevo estado de la solicitud: " + solicitud.estado)
