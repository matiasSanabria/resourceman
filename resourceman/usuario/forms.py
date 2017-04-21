# __author__ = 'matt'
#
# from django import forms
# from .models import Usuario, User
#
#
# class UserForm(forms.ModelForm):
#
#     password1 = forms.TextInput()
#     password2 = forms.TextInput()
#
#     class Meta:
#         model = User
#         REQUIRED_FIELDS = [
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'password1',
#             'password2'
#         ]
#         fields = "__all__"
#         #exclude=  [
#         #    'id',
#         #    'password',
#         #    'is_superuser',
#         #    'last_login',
#         #    'is_staff',
#         #    'is_active',
#         #   'date_joined',
#         #   'user_permissions',
#         #]
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
#             raise forms.ValidationError(u'El nombre de usuario \' %s \' ya existe.' %username)
#         else:
#             return username
#
#     def clean_password(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Los passwords no coinciden")
#         else:
#             return password1
#
#     def save(self, commit=True):
#         user = super(UserForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
#
#
# class UsuarioForm(forms.ModelForm):
#
#     class Meta:
#         model = Usuario
#         REQUIRED_FIELDS = [
#             'nro_documento',
#             'telefono',
#             'prioridad'
#             'rol_id'
#         ]
#
#     def clean_nrodocumento(self):
#         doc = self.cleaned_data['nro_documento']
#         if Usuario.objects.filter(nro_documento=doc).exists():
#             raise forms.ValidationError(u'El usuario con el nro de documento %s ya existe' % doc)
#         else:
#             return doc
#
#     def save(self, commit=True):
#         usuario = super(UsuarioForm, self).save(commit=False)
#         if commit:
#             usuario.save()
#         return usuario