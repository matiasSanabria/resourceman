
from .models import *
from django.contrib.auth.models import Permission

from django import forms

class EditarPermisos(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':4, 'cols':15}))


class ListarPermisos(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class AgregarPermiso(forms.ModelForm):
    codename = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Permission
        fields = '__all__'
        REQUIRED_FIELDS = [
            'content_type', 'codename','name',
        ]
        exclude = []