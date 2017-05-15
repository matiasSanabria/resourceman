from django import forms
from django.forms import Select, TextInput, DateInput

from ..mantenimiento.models import Mantenimiento


class MantenimientoForm(forms.ModelForm):
    """
    Formulario para los mantenimientos de recursos
    """
    def __init__(self, *args, **kwargs):
        super(Mantenimiento, self).__init__(*args, **kwargs)

    tipo_recurso = Select(attrs={'class': 'dropdown-toggle'})

    class Meta:
        model = Mantenimiento
        fields = '__all__'
        exclude = ['codigo']
        widgets = {
            'recurso': Select(attrs={'class': 'form-control'}),
            'motivo': TextInput(attrs={'class': 'form-control'}),
            'tipo_movimiento': Select(attrs={'class': 'btn dropdown-toggle'}),
            'fecha_inicio': DateInput(),
            'fecha_fin': DateInput(),
            'mantenimiento_programado': DateInput(),
            'costo': TextInput(attrs={'class': 'form-control'})
        }