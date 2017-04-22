__author__ = 'matt'

from django import forms
from .models import TipoRecurso, Estados, Recurso
from django.forms import TextInput, Textarea, Select


class TipoRecursoForm(forms.ModelForm):
    """
        Formulario para los Tipos de Recursos
    """
    class Meta:
        model = TipoRecurso
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            'descripcion': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            'lista_caracteristicas': Textarea(attrs={'rows': '5', 'class': 'form-control'}),
            'estado': Select(attrs={'class': 'btn btn-default dropdown-toggle'})
        }


class RecursoForm(forms.ModelForm):
    """
        Formulario para la clase Recurso
    """
    class Meta:
        model = Recurso
        fields = '__all__'
        widgets = {
            'codigo_recurso': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            'nombre_recurso': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            'descripcion_recurso': Textarea(attrs={'class': 'form-control', 'rows':'3'}),
            'tipo_recurso': Select(attrs={'class': 'btn btn-default dropdown-toggle'}),
            'activo': Select(attrs={'class': 'btn btn-default dropdown-toggle'})
        }


class EstadoForm(forms.ModelForm):
    """
        Formulario para la clase Estados de Recurso
    """
    class Meta:
        model = Estados
        fields = '__all__'
        widgets = {
            'codigo': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            'descripcion': Textarea(attrs={'class': 'col-lg-3 form-control', 'rows': '4'}),
        }
