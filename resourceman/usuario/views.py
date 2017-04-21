# from django.core.checks import messages
# from django.shortcuts import render, redirect
# from .forms import UserForm, UsuarioForm
#
# # Create your views here.
# def crear(request):
#     """
#     Vista de creacion de usuario
#     :param request:
#     :return:
#     """
#     if request.method == "POST":
#         user_form = UserForm(request.POST)
#         usuario_form = UsuarioForm(request.POST)
#
#         if user_form.is_valid():
#             if usuario_form.is_valid():
#                 # guardamos el objeto Model sin guardarlo en la BD
#                 usuario = user_form.save(commit=False)
#                 usuario.is_active = 1
#                 usuario.save()
#                 # guardamos el objeto Model sin guardarlo en la BD
#                 usuario_det = usuario_form.save(commit=False)
#                 # asociamos el detalle con el usuario
#                 usuario_det.usuario = usuario
#                 # se guarda en la BD
#                 usuario_det.save()
#                 messages.add_message(request, messages.SUCCESS,
#                                      "Usuario %s creado correctamente" % usuario.username)
#                 return redirect('usuario/crear_usuario.html')
#             else:
#                 user_form = UserForm()
#                 usuario_form = UsuarioForm()
#
#             return render(request, 'usuario/crear_usuario.html',
#                           {
#                               'user_form': user_form,
#                               'usuario_form':usuario_form,
#                           })