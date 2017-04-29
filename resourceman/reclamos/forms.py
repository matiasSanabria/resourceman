from .models import *
from django import forms
from django.forms import ModelForm, TextInput, Textarea
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
            'descripcion': Textarea(attrs={'class': 'form-control', 'rows': '2'})
        }
        REQUIRED_FIELDS = [
            'recurso',
            'usuario', 'descripcion', 'fecha',
        ]
        exclude = []
