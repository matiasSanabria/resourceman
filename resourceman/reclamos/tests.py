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

        reclamo = Reclamo.objects.create(
            recurso=recurso,
            usuario=models.ForeignKey(User, blank=False),
            descripcion="Exploto",
            fecha=forms.DateField(initial=datetime.datetime.now().date()),
            estado='NUE'
        )

    def testReclamo(self):
        reclamo = Reclamo.objects.get(recurso="P1")
        reclamo.estado= 'PEN'
        self.assertEqual()

    def countReclamos(self):
        nuevos = Reclamo.objects.all()
        print(nuevos.count())
