from django.test import TestCase
from django.contrib.auth.models import Group


class GroupTestCase(TestCase):
    def setUp(self):
        """
         Esto es un Group
         - fields: {name: Prueba, 
                }
        """
        Group.objects.create(name="Prueba1")


    # para ejecutar el test de objener group
    # ./manage.py test roles.tests.GrouoTestCase.obtener_group
    def obtener_group(self):
        group = Group.objects.get(nombre="Prueba1")
        print(group)
        self.assertIsNotNone(group)
        group = Group.objects.get(nombre="NOEXISTE")
        self.assertIsNone(group)