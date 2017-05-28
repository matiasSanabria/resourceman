from django.forms import TextInput, Textarea
from django import forms

from .models import RegistroUsuario


class RegistroUsuarioForm(forms.ModelForm):
    """
    Formulario para la configuracion de envios de correos de registro de usuario
    """
    class Meta:
        model = RegistroUsuario
        fields = '__all__'
        exclude = ['id']
        widgets = {
            'asunto': TextInput(attrs={'class': 'form-control col-lg-3'}),
            'mensaje': Textarea(attrs={'class': 'form-control col-lg-3', 'rows': '3'})
        }

    def save(self, commit=True):
        registro = super(RegistroUsuarioForm, self).save(commit=False)
        if commit:
            registro.save()
        return registro