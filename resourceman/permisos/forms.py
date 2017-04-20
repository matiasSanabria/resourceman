
from .models import *
from django.contrib.auth.models import Permission

from django import forms

# class ListarPermisos(forms.Form):
#
#     class Meta:
#         model = Permission
#         fields = '__all__'
#         REQUIRED_FIELDS = [
#             'content_type', 'codename', 'name',
#         ]
#         exclude = []

class EditarPermisos(forms.ModelForm):
    # codename = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    # # codigo divague
    # def __init__(self, *args, **kwargs):
    #     instance = kwargs.get('instance', None)
    #     kwargs.update(initial={
    #         # 'field': 'value'
    #         # 'permissions': '',
    #     })
    #     super(EditarPermisos, self).__init__(*args, **kwargs)

    # class Meta:
    #     model = Roles
    #     fields = '__all__'
    #     REQUIRED_FIELDS = [
    #         'name', 'permissions',
    #     ]
    #     exclude = []
    #

    # clase para extender
    class Meta:
        model = Permission
        fields = '__all__'
        REQUIRED_FIELDS = [
            'content_type', 'codename', 'name',
        ]
        exclude = []

class AgregarPermiso(forms.ModelForm):
    codename = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    #clase para extender
    class Meta:
        model = Permission
        fields = '__all__'
        REQUIRED_FIELDS = [
            'content_type', 'codename','name',
        ]
        exclude = []