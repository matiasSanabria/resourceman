from dal import autocomplete
from django import forms
from .models import Reservas, SolicitudReservas
from django.forms import TextInput, Textarea, Select, DateInput

__author__ = 'hector'


class ReservasForm(forms.ModelForm):
    """
    Formulario para reservas
    """

    class Meta:
        model = Reservas
        fields = '__all__'
        REQUIRED_FIELDS = [
             'hora_ini', 'hora_fin', 'tipo_recurso','recurso', 'descripcion',
        ]
        widgets = {
            'tipo_recurso': Select(attrs={'class': 'btn dropdown-toggle'}),
            'recurso': autocomplete.ModelSelect2(url='recu_by_tipo-autocomplete',
                                                 forward=['tipo_recurso','hora_ini','hora_fin']),
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


class SolicitudForm(forms.ModelForm):
    """
    Formulario para reservas
    """
    # fecha_reserva = DateField(input_formats=['%d/%m/%Y'])
    # fecha_reserva = DateInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/YYYY'})
    class Meta:
        model = SolicitudReservas
        fields = '__all__'
        REQUIRED_FIELDS = [
            'hora_ini', 'hora_fin', 'tipo_recurso', 'recurso', 'descripcion', 'fecha_reserva',
        ]
        widgets = {
            'tipo_recurso': Select(attrs={'class': 'btn dropdown-toggle'}),
            'recurso': autocomplete.ModelSelect2(url='solicitud-autocomplete',
                                                 forward=['tipo_recurso']),
            # 'fecha_reserva': DateInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/YYYY'}),
            'fecha_reserva': DateInput(attrs={'class': 'datepicker'}),
            'hora_ini': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            'hora_fin': TextInput(attrs={'class': 'col-lg-3 form-control'}),
            'descripcion': Textarea(attrs={'rows': '3', 'class': 'form-control'}),
        }
        exclude = ['fecha_solicitud', 'usuario', 'estado']

    def save(self, commit=True):
        solicitud = super(SolicitudForm, self).save(commit=False)
        if commit:
            solicitud.save()
        return solicitud
