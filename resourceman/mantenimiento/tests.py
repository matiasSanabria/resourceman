from django.test import TestCase
from .models import Mantenimiento
from tipos_recursos.models import TipoRecurso, Recurso, Estados


class MantenimientoTestCase(TestCase):
    def setUp(self):
        print("Iniciando test de mantenimiento")
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

        mantenimiento = Mantenimiento.objects.create(
            tipo_recurso=tipo_recurso,
            recurso=recurso,
            motivo="Test de Mantenimiento",
            tipo_mantenimiento="PRE",
            fecha_inicio="2017-06-01",
            fecha_fin="2017-06-05",
            costo="100000",
            estado=estado_recurso.codigo
        )
        print("mantenimiento creado: " + mantenimiento.tipo_recurso.descripcion + '\n'
                                       + mantenimiento.recurso.nombre_recurso + '\n'
                                       + mantenimiento.estado + '\n'
                                       + mantenimiento.motivo + '\n'
                                       + mantenimiento.tipo_mantenimiento + '\n'
                                       + mantenimiento.fecha_inicio + '\n'
                                       + mantenimiento.fecha_fin + '\n'
                                       + mantenimiento.costo)

    def testMantenimiento(self):
        mantenimiento = Mantenimiento.objects.get(recurso="P1")
        self.assertIsNotNone(mantenimiento)
        self.assertEqual(mantenimiento.tipo_recurso.nombre, "PRO")
