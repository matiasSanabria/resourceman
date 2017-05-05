from .models import *
from django import forms
from django.forms import ModelForm, TextInput, Textarea, Select
import datetime

class CrearReclamo(forms.ModelForm):
    # aqui se config el campo de fecha
    # fecha = forms.DateTimeField(initial=datetime.datetime.now())
    fecha = forms.DateField(initial=datetime.datetime.now().date())
    class Meta:
        model = Reclamo
        fields = '__all__'
        widgets = {
            'recurso': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            'descripcion': Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }
        REQUIRED_FIELDS = [
            'recurso', 'descripcion'
        ]
        exclude = []

class EditarReclamo(forms.ModelForm):
    recurso = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Reclamo
        fields = '__all__'
        REQUIRED_FIELDS = [
            'recurso', 'descripcion', 'estado',
        ]
        widgets = {
            'estado': Select(attrs={'class': 'btn dropdown-toggle'})
        }
        exclude = []

