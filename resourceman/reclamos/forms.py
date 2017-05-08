from .models import *
from django import forms
from django.forms import ModelForm, TextInput, Textarea, Select
import datetime

class CrearReclamo(ModelForm):
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
        exclude = ['usuario', 'estado']

    def save(self, commit=True):
        reclamo = super(CrearReclamo, self).save(commit=False)
        if commit:
            reclamo.save()
        return reclamo

class EditarReclamo(ModelForm):

    class Meta:
        model = Reclamo
        fields = '__all__'
        REQUIRED_FIELDS = [
            'recurso', 'descripcion', 'estado',
        ]
        widgets = {
            'estado': Select(attrs={'class': 'btn dropdown-toggle'}),
            'recurso': forms.TextInput({'class': 'form-control','readonly': 'readonly'}),
            'descripcion': forms.Textarea({'class': 'form-control','readonly': 'readonly', 'rows':'3'}),
        }
        exclude = ['usuario']

