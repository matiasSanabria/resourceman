from django.test import TestCase
from ..mantenimiento.models import Mantenimiento
from ..tipos_recursos.models import TipoRecurso, Recurso, Estados


class MantenimientoTestCase(TestCase):
    def setUp(self):
        tipo_recurso = TipoRecurso.objects.create(
            nombre="PRO",
            descripcion="PROYECTOR",
            lista_caracteristicas='{"codigo": "varchar2(10)"}, {"marca": "varchar2(10)"}',
            estado='A'
        )

        estado_recurso = Estados.objects.create(
            codigo="DIS",
            descripcion="DISPONIBLE"
        )

        recurso = Recurso.objects.create(
            codigo_recurso="P1",
            nombre_recurso="Proyector 1",
            tipo_recurso=tipo_recurso,
            estado=estado_recurso
        )

        mantenimiento = Mantenimiento.objects.create(
            tipo_recurso=tipo_recurso,
            recurso=recurso,
            motivo="Test de Mantenimiento",
            tipo_mantenimiento="PRE",
            fecha_inicio="01/06/2017",
            fecha_fin="02/06/2017",
            mantenimiento_programado="01/01/2018",
            costo="100000",
            estado=estado_recurso
        )

    def testMantenimiento(self):
        mantenimiento = Mantenimiento.objects.get(recurso="P1")
        self.assertEqual(mantenimiento.tipo_recurso, "PRO")
