from django.test import TestCase
from .views import *


# Create your tests here.

class FormPermisosTest(TestCase):
    # Valid Form Data
    def agregarPermisoFTV(self):
        form = AgregarPermiso(data={'content_type': "log entry", 'codename': 1, 'name': "entrar"})
        form.save()
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def agregarPermisoFTI(self):
        form = AgregarPermiso(data={'content_type': "", 'codename': 1, 'name': ""})
        self.assertTrue(form.is_valid())

    # Valid Form Data
    def editarPermisoFTV(self):
        form = EditarPermisos(data={'content_type': "log entry", 'codename': 1, 'name': "entrar"})
        form.save()
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def editarPermisoFTI(self):
        form = EditarPermisos(data={'content_type': "log entry", 'codename': 1, 'name': "entrar"})
        self.assertTrue(form.is_valid())


class ViewPermisosTest(TestCase):
    # Valid Data
    def agregarPermisoVTV(self):
        permission_count = Permission.objects.count()
        agregar_form = AgregarPermiso(data={'content_type': "log entry", 'codename': 1, 'name': "entrar"})
        agregar_form.save()
        self.assertEqual(agregar_form.status_code, 200)
        self.assertEqual(Permission.objects.count(), permission_count + 1)
        self.assertTrue('"error": false' in agregar_form.content)

    def editarPermisoVTV(self, param):
        permiso = Permission.objects.get(id=param)
        editar_form = EditarPermisos(data={'content_type': "log entry", 'codename': 1, 'name': "entrar"}, instance=param)
        editar_form.save()
        self.assertEqual(permiso.status_code, 200)
        self.assertTrue('"error": false' in permiso.content)

    def eliminarPermisoVTV(self, param):
        permission_count = Permission.objects.count()
        permiso = Permission.objects.get(id=param)
        permiso.delete()
        self.assertEqual(permiso.status_code, 200)
        self.assertEqual(Permission.objects.count(), permission_count - 1)
        self.assertTrue('"error": false' in permiso.content)
