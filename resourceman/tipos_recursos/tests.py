from django.test import TestCase
from .forms import  *
from .models import *
from .views import *

# Create your tests here.

class TipoRecursosTest(TestCase):

    def tipoRecursosFTV(self):
        tipo_recurso = TipoRecursoForm(data={'nombre': "", 'descripcion': "",'lista_caracteristicas': "",'estado': ""})
        self.assertTrue(form.is_valid())
        tipo_recurso.save()

    def crearVTV(self):
        tipo_recurso_count = TipoRecurso.objects.count()
        tipo_recurso = TipoRecursoForm(data={'nombre': "", 'descripcion': "",'lista_caracteristicas': "",'estado': ""})
        self.assertEqual(tipo_recurso.status_code, 200)
        self.assertEqual(TipoRecurso.objects.count(), tipo_recurso_count + 1)
        self.assertTrue('"error": false' in tipo_recurso.content)
        tipo_recurso.save()

    def editarVTV(self, param):
        editar = TipoRecurso.objects.get(nombre=param)
        editar_form = TipoRecursoForm(
            data={'nombre': "", 'descripcion': "", 'lista_caracteristicas': "", 'estado': ""},instance=editar)
        self.assertEqual(editar.status_code, 200)
        self.assertTrue('"error": false' in editar.content)
        editar_form.save()

    def eliminarVTV(self, param):
        tipo_recurso_count = TipoRecurso.objects.count()
        eliminar = TipoRecurso.objects.get(nombre=param)
        eliminar.delete()
        self.assertEqual(eliminar.status_code, 200)
        self.assertEqual(TipoRecurso.objects.count(), tipo_recurso_count - 1)
        self.assertTrue('"error": false' in eliminar.content)
