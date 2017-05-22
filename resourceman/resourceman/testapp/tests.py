from django.test import TestCase
from resourceman.resourceman.login.forms import LoginForm
from resourceman.resourceman.permisos.forms import AgregarPermiso, EditarPermisos
from resourceman.resourceman.roles.forms import AgregarRol, EditarRol
from resourceman.resourceman.tipos_recursos.forms import *
from resourceman.resourceman.usuarios.forms import *
from resourceman.resourceman.reservas.forms import *

import urllib, base64, tempfile, datetime

# Create your tests here.

class MainTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('admin', 'admin@world.com', 'admin')
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.is_active = True
        self.user.save()
        self.auth_string = 'Basic %s' % base64.encodestring('admin:admin').rstrip()

    def tearDown(self):
        self.user.delete()

