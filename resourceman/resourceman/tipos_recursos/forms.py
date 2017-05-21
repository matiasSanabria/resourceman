from django.forms.formsets import BaseFormSet

__author__ = 'matt'

from django import forms
from .models import TipoRecurso, Estados, Recurso, Encargado, CaracteristicasRecursos
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


class CaracteristicasRecursosForm(forms.ModelForm):

    class Meta:
        model = CaracteristicasRecursos
        fields = ['clave', 'valor']
        widgets = {
            'clave': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            'valor': TextInput(attrs={'class': 'col-lg-3 form-control'}),
        }


class CaracteristicasRecursosFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return

        claves = []
        valores = []
        duplicados = False

        for form in self.forms:
            if form.cleaned_data:
                clave = form.cleaned_data['clave']
                valor = form.cleaned_data['valor']

                if clave and valor:
                    if valor in claves:
                        duplicados = True
                    claves.append(valor)

                    if valor in valores:
                        duplicados = True
                    valores.append(valor)

                if duplicados:
                    raise forms.ValidationError()


class RecursoForm(forms.ModelForm):
    """
    Formulario para la clase Recurso
    """
    list = TipoRecurso.lista_caracteristicas

    class Meta:
        model = Recurso
        fields = '__all__'
        widgets = {
            'codigo_recurso': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            'nombre_recurso': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            'tipo_recurso': Select(attrs={'class': 'btn btn-default dropdown-toggle'}),
            'estado': Select(attrs={'class': 'btn btn-default dropdown-toggle'}),
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
            'descripcion': TextInput(attrs={'class': 'col-lg-3 form-control'}),
        }


class EncargadoForm(forms.ModelForm):
    """
    Formulario para la clase Estados de Recurso
    """
    def __init__(self, *args, **kwargs):
        # instance = kwargs.get('instance', None)
        # kwargs.update(initial={
        #     # 'field': 'value'
        #     'dni': '5214801',
        #     'category': 'NON',
        #     'phone': '527-622',
        # })
        super(EncargadoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Encargado
        fields = '__all__'
        REQUIRED_FIELDS = [
            'usuario'
        ]
        widgets = {
            'usuario': Select(attrs={'class': 'btn dropdown-toggle'}),
        }
        exclude = ['tipo_recurso']

    def save(self, commit=True):
        encargado = super(EncargadoForm, self).save(commit=False)
        if commit:
            encargado.save()
        return encargado
