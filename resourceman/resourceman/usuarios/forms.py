__author__ = 'hector'

from django.forms.extras.widgets import SelectDateWidget

import datetime
from django import forms
from django.forms import widgets, TextInput
from django.contrib.auth.models import User
from django.utils import timezone

from django import forms
from django.forms import Select


from .models import *

class UsuarioCreationForm(forms.ModelForm):
    """
        UsuarioCreationForm ModelForm para la creacion de usuarios, con campos de User.

        Muestra campos del model User en inputs de HTML.

        *Campos:* Los establecidos en User.

        1. ``id``
        #. ``password``
        #. ``is_superuser``
        #. ``username``
        #. ``first_name``
        #. ``last_name``
        #. ``email``.
        #. ``is_active``
        #. ``date_joined``


    """
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}), initial='password')
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control'}), initial='password')

    def __init__(self, *args, **kwargs):
        # instance = kwargs.get('instance', None)
        # kwargs.update(initial={
        #     # 'field': 'value'
        #     'username': 'daniel',
        #     'first_name': 'daniel',
        #     'last_name': 'min',
        #     'email': 'dpark8752@gmail.com',
        # })
        super(UsuarioCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        # fields = ('username', 'first_name', 'last_name', 'email')
        help_texts = {
            'username': ''
        }
        REQUIRED_FIELDS = [
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2',
        ]
        exclude = [
            'id', 'password', 'is_superuser', 'is_staff', 'last_login', 'date_joined',
            'user_permissions', 'is_active',
        ]
        widgets = {
            'email': TextInput(attrs={'class': 'form-control'})
        }


    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario \'%s\' ya está en uso.' % username)
        else:
            return username

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        else:
            return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UsuarioCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UsuarioDetalleForm(forms.ModelForm):
    """
        UsuarioDetalleForm ModelForm para la creacion de usuarios, con campos de Usuario.

        Muestra campos del model Usuario en inputs de HTML.

        *Campos:* Los establecidos en Usuario.

        1. ``nro_documento``
        #. ``direccion``
        #. ``telefono``
        #. ``prioridad``


    """
    nro_documento = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    direccion = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows': '3'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        # instance = kwargs.get('instance', None)
        # kwargs.update(initial={
        #     # 'field': 'value'
        #     'dni': '5214801',
        #     'category': 'NON',
        #     'phone': '527-622',
        # })
        super(UsuarioDetalleForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Usuario
        # fields = ('usuario', 'nro_doucmento', 'prioridad', 'telefono', 'direccion')
        REQUIRED_FIELDS = [
            'nro_documento','prioridad','direccion','telefono'
        ]
        widgets = {
                'prioridad': Select(attrs={'class': 'btn dropdown-toggle'})
            }
        exclude = ['usuario']

    def clean_dni(self):
        nro_documento = self.cleaned_data['nro_documento']
        if Usuario.objects.filter(nro_documento=nro_documento).exists():
            raise forms.ValidationError('Usuario con el DNI %s ya existe.' % nro_documento)
        else:
            return nro_documento

    def save(self, commit=True):
        user_detail = super(UsuarioDetalleForm, self).save(commit=False)
        if commit:
            user_detail.save()
        return user_detail

class UserInfoForm(forms.ModelForm):
    """
        UserInfoForm ModelForm para la edicion de usuarios, con campos de User.

        Muestra campos del model User en el HTML, para su edicion.

        *Campos:* Los establecidos en User.

        1. ``id``
        #. ``password``
        #. ``last_login``:
        #. ``is_superuser``
        #. ``username``
        #. ``first_name``
        #. ``last_name``
        #. ``email``.
        #. ``is_active``
        #. ``date_joined``

    """
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_joined = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = '__all__'
        help_texts = {
            'username': ''
        }
        widgets = {
            'email': TextInput(attrs={'class': 'form-control'})
        }
        exclude = [
             'user_permissions', 'password'
        ]

class UsuarioInfoForm(forms.ModelForm):
    """
        UsuarioInfoForm ModelForm para la edicion de usuarios, con campos de Usuario.

        Muestra campos del model Usuario en el HTML, para su edicion.

        *Campos:* Los establecidos en Usuario.

        1. ``nro_documento``
        #. ``direccion``
        #. ``telefono``
        #. ``prioridad``


    """
    nro_documento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'prioridad': Select(attrs={'class': 'btn dropdown-toggle'})
        }
        exclude = [
            'usuario',
        ]


class AgregarPrioridad(forms.ModelForm):
    """
        AgregarPrioridad ModelForm para la creacion de prioridades, con campos de PrioridadUsuario.

        Muestra campos del model PrioridadUsuario en inputs de HTML.

        *Campos:* Los establecidos en PrioridadUsuario.

        1. ``codigo``
        #. ``descipcion``


    """
    codigo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = PrioridadUsuario
        REQUIRED_FIELDS = [
            'codigo', 'descripcion'
        ]
        exclude = []

class EditarPrioridad(forms.ModelForm):
    """
        EditarPrioridad ModelForm para la edicion de prioridades, con campos de PrioridadUsuario.

        Muestra campos del model PrioridadUsuario en HTML, para su edicion.

        *Campos:* Los establecidos en PrioridadUsuario.

        1. ``codigo``
        #. ``descipcion``


    """
    codigo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = PrioridadUsuario
        REQUIRED_FIELDS = [
            'codigo', 'descripcion'
        ]
        exclude = []
