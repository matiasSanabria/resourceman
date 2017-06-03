from django.test import TestCase
from django.contrib.auth.models import User
from .models import Reclamo
from tipos_recursos.models import TipoRecurso, Recurso, Estados
import datetime


class ReclamoTestCase(TestCase):
    def setUp(self):
        print("Iniciando test de reclamos\n")

        tipo_recurso = TipoRecurso.objects.create(
            nombre="PRO",
            descripcion="PROYECTOR",
            lista_caracteristicas='{"codigo": "varchar2(10)"}, {"marca": "varchar2(10)"}',
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

        reclamo = Reclamo.objects.create(
            recurso=recurso,
            usuario=usuario,
            descripcion='test de reclamos',
            fecha=datetime.date.today(),
        )
        print("reclamo creado: " + reclamo.recurso.nombre_recurso + '\n'
                                 + reclamo.descripcion + '\n'
                                 + reclamo.usuario.username + '\n'
                                 + reclamo.fecha.__str__() + '\n')

    def testReclamo(self):
        reclamo = Reclamo.objects.get(recurso="P1")
        self.assertNotEqual(reclamo.recurso.codigo_recurso, 'P2')

    def countReclamos(self):
        nuevos = Reclamo.objects.all()
        print(nuevos.count())
