
from .models import *
from django.contrib.auth.models import Permission

from django import forms

from django.forms import Select

# class ListarPermisos(forms.Form):
#
#     class Meta:
#         model = Permission
#         fields = '__all__'
#         REQUIRED_FIELDS = [
#             'content_type', 'codename', 'name',
#         ]
#         exclude = []

class EditarPermisos(forms.ModelForm):
    codename = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Permission
        fields = '__all__'
        REQUIRED_FIELDS = [
            'content_type', 'codename', 'name',
        ]
        widgets = {
            'content_type': Select(attrs={'class': 'btn dropdown-toggle'})
        }
        exclude = []

class AgregarPermiso(forms.ModelForm):
    codename = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    #clase para extender
    class Meta:
        model = Permission
        fields = '__all__'
        REQUIRED_FIELDS = [
            'content_type', 'codename','name',
        ]
        widgets = {
            'content_type': Select(attrs={'class':'btn dropdown-toggle'})
        }
        exclude = []