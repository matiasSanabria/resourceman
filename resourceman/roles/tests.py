from django.test import TestCase
from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from .forms import *
from .views import *

# Create your tests here.

class formRolTest(TestCase):
    # Valid Form Data
    def agregarRolFTV(self):
        form = AgregarRol(data={'name': "ROL1", 'permissions': {1,2,3,4,5} })
        self.assertTrue(form.is_valid())
        form.save()

    # Invalid Form Data
    def agregarRolFTI(self):
        form = AgregarRol(data={'name': "", 'permissions': {0} })
        self.assertTrue(form.is_valid())

    # Valid Form Data
    def editarRolFTV(self):
        form = EditarRol(data={'name': "ROL1", 'permissions': {6,7,8,9,10} })
        self.assertTrue(form.is_valid())
        form.save()

    # Invalid Form Data
    def editarRolFTI(self):
        form = EditarRol(data={'name': "", 'permissions': {0} })
        self.assertTrue(form.is_valid())


class viewRolTest(TestCase):
    # Valid Data
    def agregarRolVTV(self):
        rol_count = Group.objects.count()
        agregar_form = AgregarRol(data={'name': "ROL1", 'permissions': {6,7,8,9,10} })
        agregar_form.save()
        self.assertEqual(agregar_form.status_code, 200)
        self.assertEqual(Group.objects.count(), rol_count + 1)
        self.assertTrue('"error": false' in agregar_form.content)

    def editarRolVTV(self, param):
        rol = Group.objects.get(id=param)
        agregar_form = AgregarRol(data={'name': "ROL1", 'permissions': {6, 7, 8, 9, 10} }, instance=param)
        agregar_form.save()
        self.assertEqual(rol.status_code, 200)
        self.assertTrue('"error": false' in rol.content)

    def eliminarRolVTV(self, param):
        rol_count = Group.objects.count()
        rol = Group.objects.get(id=param)
        rol.delete()
        self.assertEqual(rol.status_code, 200)
        self.assertEqual(Permission.objects.count(), rol_count - 1)
        self.assertTrue('"error": false' in rol.content)
