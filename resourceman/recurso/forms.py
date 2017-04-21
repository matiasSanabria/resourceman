__author__ = 'matt'

from .models import Recurso
from django import forms
from django.forms import TextInput, Textarea, Select


class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = '__all__'
        widgets = {
            'codigo_recurso': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            'descripcion_recurso': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            #'tipo_recurso': Textarea(attrs={'rows': '5', 'class': 'form-control'}),
            'estado_recurso': Select(attrs={'class': 'btn btn-default dropdown-toggle'})
        }