
__author__ = 'matt'

from django import forms
from .models import TipoRecurso
from django.forms import TextInput, Textarea


class TipoRecursoForm(forms.ModelForm):
    class Meta:
        model = TipoRecurso
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            'descripcion': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            'lista_caracteristicas': Textarea(attrs={'rows': '5', 'class': 'form-control'})
        }