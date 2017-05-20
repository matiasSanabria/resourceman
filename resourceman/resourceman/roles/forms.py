__author__ = 'hector'

from django.contrib.auth.models import Group, GroupManager, Permission
from django.db import models
from django import forms

from django.forms import Select, SelectMultiple


class AgregarRol(forms.ModelForm):
    """
    AgregarRol ModelForm para la creacion de roles, con campos de Group.

    Muestra campos del model Group en inputs de HTML.

    *Campos:* Los establecidos en Group.

    1. ``id``:
    #. ``name``:
    #. ``Permission``:
        """

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:

        model = Group
        fields = '__all__'
        REQUIRED_FIELDS = [
             'name', 'permissions',
        ]
        widgets = {'permissions': forms.CheckboxSelectMultiple}
        exclude = []

class EditarRol(forms.ModelForm):
    """
    EditarRol ModelForm para la edicion de Roles, con campos de Group.

    Muestra campos del model Group en inputs de HTML con sus valores para luego ser modificado.

    *Campos:* Los establecidos en Group.

    1. ``id``:
    #. ``name``:
    #. ``Permission``:
    """

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Group
        fields = '__all__'
        REQUIRED_FIELDS = [
            'name', 'permissions',
        ]
        widgets = {'permissions': forms.CheckboxSelectMultiple}
        exclude = []
