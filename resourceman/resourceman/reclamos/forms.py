from .models import *
from django import forms
from django.forms import Textarea, Select, DateInput, TextInput
import datetime

class CrearReclamo(forms.ModelForm):
    """
    Formulario para crear un nuevo reclamo
    """
    fecha = forms.DateField(initial=datetime.datetime.now().date())
    class Meta:
        model = Reclamo
        fields = '__all__'
        widgets = {
            'recurso': Select(attrs={'class': 'btn dropdown-toggle'}),
            'descripcion': Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }
        REQUIRED_FIELDS = [
            'recurso', 'descripcion'
        ]
        exclude = ['usuario', 'estado']

    def save(self, commit=True):
        reclamo = super(CrearReclamo, self).save(commit=False)
        if commit:
            reclamo.save()
        return reclamo

class EditarReclamo(forms.ModelForm):
    """
    Formulario para edicion de un reclamo. Solamente se permite cambiar el estado del reclamo
    """
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))

    class Meta:
        model = Reclamo
        fields = '__all__'
        REQUIRED_FIELDS = [
            'recurso', 'descripcion', 'estado',
        ]
        widgets = {
            'recurso': TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'readonly': 'readonly'}),
            'estado': Select(attrs={'class': 'btn dropdown-toggle'}),
            'fecha': DateInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
        }
        exclude = ['usuario']

