from dal import autocomplete
from django import forms
from ..reservas.models import Reservas
from django.forms import TextInput, Textarea, Select

__author__ = 'hector'


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