from django import forms
from django.forms import Select, TextInput, DateInput

from ..tipos_recursos.models import TipoRecurso
from ..mantenimiento.models import Mantenimiento


class MantenimientoForm(forms.ModelForm):
    """
    Formulario para los mantenimientos de recursos
    """
    def __str__(self, *args, **kwargs):
        return self.recurso

    class Meta:
        model = Mantenimiento
        fields = '__all__'
        exclude = ['']
        widgets = {
            'tipo_recurso': Select(attrs={'class': 'col-lg-3 form-control'}),
            'recurso': Select(attrs={'class': 'col-lg-3 form-control'}),
            'motivo': TextInput(attrs={'class': 'form-control'}),
            'tipo_mantenimiento': Select(attrs={'class': 'col-lg-3 form-control'}),
            'fecha_inicio': DateInput(attrs={'class': 'form-control'}),
            'fecha_fin': DateInput(attrs={'class': 'form-control'}),
            'mantenimiento_programado': DateInput(attrs={'class': 'form-control'}),
            'costo': TextInput(attrs={'class': 'form-control'})
        }

    def save(self, commit=True):
        mantenimiento = super(MantenimientoForm, self).save(commit=False)
        if commit:
            mantenimiento.save()
        return mantenimiento
