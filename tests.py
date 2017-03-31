import django
from django.test import TestCase
import unittest
from models import AuthGroup

class AuthGroupTestCase(unittest.TestCase):
	def testCrearGrupo(self):		
		self.grupo = AuthGroup(name="prueba")
		print "Nombre del Grupo: " + self.grupo.name
		self.grupo.save()