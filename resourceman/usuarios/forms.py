

from django.forms.extras.widgets import SelectDateWidget

import datetime
from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.utils import timezone

from django import forms
from django.forms import Select


from .models import *

class UsuarioCreationForm(forms.ModelForm):


    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}), initial='password')
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control'}), initial='password')

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
        # widgets = {
        #     'groups': Select(attrs={'class': 'btn dropdown-toggle'})
        # }


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


    nro_documento = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    direccion = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

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
    # def __init__(self, *args, **kwargs):
    #     # instance = kwargs.get('instance', None)
    #     # kwargs.update(initial={
    #     #     # 'field': 'value'
    #     #     'username': 'daniel',
    #     #     'first_name': 'daniel',
    #     #     'last_name': 'min',
    #     #     'email': 'dpark8752@gmail.com',
    #     # })
    #     super(UserInfoForm, self).__init__(*args, **kwargs)
    #     # Hacer solo lectura los cammpos fecha de alta y ultima sesion
    #     self.fields['last_login'].widget.attrs['readonly'] = True
    #     self.fields['date_joined'].widget.attrs['readonly'] = True

    class Meta:
        model = User
        fields = '__all__'
        help_texts = {
            'username': ''
        }
        exclude = [
             'user_permissions', 'password'
        ]

class UsuarioInfoForm(forms.ModelForm):


    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = [
            'usuario',
        ]


class AgregarPrioridad(forms.ModelForm):

    class Meta:
        model = PrioridadUsuario
        REQUIRED_FIELDS = [
            'codigo', 'descripcion'
        ]
        exclude = []

class EditarPrioridad(forms.ModelForm):

    class Meta:
        model = PrioridadUsuario
        REQUIRED_FIELDS = [
            'codigo', 'descripcion'
        ]
        exclude = []
