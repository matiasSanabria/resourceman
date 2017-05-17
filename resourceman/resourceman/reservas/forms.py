from dal import autocomplete
from django.forms.formsets import BaseFormSet

__author__ = 'hector'

from django import forms
# from django.forms import Time
# from .models import  Reservas
from ..tipos_recursos.models import TipoRecurso
from ..reservas.models import Reservas
from django.forms import TextInput, Textarea, Select, models, TimeInput, DateInput


class ReservasForm(forms.ModelForm):
    """
    Formulario para reservas
    """

    class Meta:
        model = Reservas
        fields = '__all__'
        REQUIRED_FIELDS = [
            'tipo_recurso','recurso', 'hora_ini', 'hora_fin', 'descripcion',
        ]
        widgets = {
            'tipo_recurso': Select(attrs={'class': 'btn dropdown-toggle'}),
            'recurso': autocomplete.ModelSelect2(url='recu_by_tipo-autocomplete',
                                                 forward=['tipo_recurso']),
            'hora_ini': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            'hora_fin': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            'descripcion': Textarea(attrs={'rows': '3', 'class': 'form-control'}),
        }
        exclude = ['fecha', 'usuario', 'estado']

    def save(self, commit=True):
        reserva = super(ReservasForm, self).save(commit=False)
        if commit:
            reserva.save()
        return reserva