from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
from reclamos.models import Reclamo
from tipos_recursos.models import TipoRecurso, Recurso, Estados
import datetime
from django import forms
# Create your tests here.

class ReclamoTestCase(TestCase):
    def setUp(self):
        reclamo = Reclamo.objects.create(
            recurso=models.ForeignKey(Recurso, blank=False, null=False),
            usuario=models.ForeignKey(User, blank=False),
            descripcion="Exploto",
            fecha=forms.DateField(initial=datetime.datetime.now().date()),
            estado='NUE'
        )


    def testReclamo(self):
        reclamo = Reclamo.objects.get(recurso='1')
        reclamo.estado= 'PEN'
        self.assertEqual()from django.test import TestCase

# Create your tests here.
