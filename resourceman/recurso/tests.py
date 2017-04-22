from django.test import TestCase
from .forms import *
from .models import *
from .views import *

# Create your tests here.

class RecursoFormTest(TestCase):
    def recursoFTV(self):
        form = RecursoForm(data={'codigo_recurso': 1, 'descripcion_recurso': "proyector", 'estado_recurso': "default"})
        form.save()

    def recursoVTV(self):
        count = Recurso.objects.count()
        form = RecursoForm(data={'codigo_recurso': 1, 'descripcion_recurso': "proyector", 'estado_recurso': "default"})
        form.save()
        self.assertEqual(form.status_code, 200)
        self.assertEqual(Recurso.objects.count(), count + 1)
        self.assertTrue('"error": false' in form.content)
