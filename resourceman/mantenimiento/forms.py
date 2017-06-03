from dal import autocomplete
from django import forms
from django.forms import Select, TextInput, DateInput
from .models import Mantenimiento


class MantenimientoForm(forms.ModelForm):
    """
    Formulario para los mantenimientos de recursos
    """

    class Meta:
        model = Mantenimiento
        fields = '__all__'
        exclude = ['estado', 'tipo_mantenimiento']
        widgets = {
            'tipo_recurso': Select(attrs={'class': 'col-lg-3 form-control'}),
            'recurso': autocomplete.ModelSelect2(url='mant_by_rec-autocomplete',
                                                 forward=['tipo_recurso']),
            'motivo': TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': DateInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/YYYY'}),
            'fecha_fin': DateInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/YYYY'}),
            'costo': TextInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        mantenimiento = super(MantenimientoForm, self).save(commit=False)
        if commit:
            mantenimiento.save()
        return mantenimiento
