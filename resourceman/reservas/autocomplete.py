from dal import autocomplete

from tipos_recursos.models import Recurso
from .models import Reservas
from datetime import datetime


class RecursoByTipoRecursoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        print("crear recurso//////////")
        if not self.request.user.is_authenticated():
            return Recurso.objects.none()

        recurso = Recurso.objects.all().exclude(estado__descripcion="EN MANTENIMIENTO"
                                                ).exclude(estado__descripcion="FUERA DE USO"
                                                          ).order_by('nombre_recurso')
        # print(recurso)
        tipo_recurso = self.forwarded.get('tipo_recurso', None)
        reservados = Reservas.objects.filter(tipo_recurso=tipo_recurso).filter(
                                                    fecha=datetime.now().date()
                                            ).exclude(estado='TE').exclude(estado='CA')
        inicio = self.forwarded.get('hora_ini')
        fin = self.forwarded.get('hora_fin')
        inicio = datetime.strptime(inicio, '%H:%M').time()
        fin = datetime.strptime(fin, '%H:%M').time()
        print(inicio)
        recurso2 = []
        if tipo_recurso and inicio and fin:
            if inicio < fin and inicio >= datetime.strptime('07:00', '%H:%M').time() and fin <= datetime.strptime('22:00', '%H:%M').time():
                recurso = recurso.filter(tipo_recurso=tipo_recurso)
                if reservados:
                    reservados2 = []
                    for rese in reservados:
                        if inicio >= rese.hora_fin and fin >= rese.hora_ini:
                            print("No hay conflicto")
                        else:
                            reservados2.append(rese)
                            print("Conflicto")
                    for recu in recurso:
                        recurso2.append(recu)
                    for reser in reservados2:
                        ubicacion = recurso2.index(reser.recurso)
                        del recurso2[ubicacion]
                else:
                    recurso2 = recurso
            else:
                return recurso.none()
        else:
            return recurso.none()
        if self.q:
            recurso2 = recurso2.filter(nombre_recurso__icontains=self.q)

        return recurso2


class SolicitudAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Recurso.objects.none()

        recurso = Recurso.objects.all().exclude(estado__descripcion="FUERA DE USO"
                                                          ).order_by('nombre_recurso')
        print(recurso)
        tipo_recurso = self.forwarded.get('tipo_recurso', None)
        if tipo_recurso:
            recurso = recurso.filter(tipo_recurso=tipo_recurso)
            print(recurso)
        else:
            return recurso.none()
        if self.q:
            recurso = recurso.filter(nombre_recurso__icontains=self.q)

        return recurso