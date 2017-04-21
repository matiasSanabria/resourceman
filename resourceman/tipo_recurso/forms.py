
__author__ = 'matt'

from django import forms
from .models import TiposRecursos

class TipoRecursoForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'col-lg-3 form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class':'col-lg-3 form-control'}))
    lista_caracteristicas = forms.CharField(widget=forms.Textarea(attrs={'rows': '5', 'class': 'form-control'}))

    class Meta:
        model = TipoRecurso
        fields = '__all__'