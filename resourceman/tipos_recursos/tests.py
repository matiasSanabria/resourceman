from django.test import TestCase
from .models import TipoRecurso, Estados


class TipoRecursoTestCase(TestCase):
    def setUp(self):
        """
        Esto es un tipo de recurso
        - fields: {nombre: NOTEBOOK, descripcion: NOTEBOOK, lista_caracteristicas: '{"marca":"character varying(10), '
        '"pantalla_pulgadas":"biginteger",''"procesador":"character varying(20)",''"memoria_ram": "character varying(20)"}'}
        """
        TipoRecurso.objects.create(
            nombre="LABORATORIO_2",
            descripcion="LABORATORIO DE INFORMATICA BLOQUE G",
            lista_caracteristicas='{"cantidad":"biginteger", ''"encargado":"character_variyin(20)",''"split":"biginteger",''"sillas": "biginteger"}'
        )

        Estados.objects.create(codigo="AUX", descripcion="DISPONIBLE")

    # para ejecutar el test de objener recurso
    # ./manage.py test tipos_recursos.tests.TipoRecursoTestCase.obtener_tipo_recurso
    def obtener_tipo_recurso(self):
        tipo_recurso = TipoRecurso.objects.get(nombre="NOTEBOOK")
        print(tipo_recurso)
        self.assertIsNotNone(tipo_recurso)
        tipo_recurso = TipoRecurso.objects.get(nombre="NOEXISTE")
        self.assertIsNone(tipo_recurso)