from dal import autocomplete

from ..tipos_recursos.models import Recurso


class RecursoByTipoRecursoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Recurso.objects.none()

        qs = Recurso.objects.all().exclude(estado__descripcion="EN MANTENIMIENTO").exclude(estado__descripcion="FUERA DE USO")
        tipo_recurso = self.forwarded.get('tipo_recurso', None)
        print(tipo_recurso)
        if tipo_recurso:
            qs = qs.filter(tipo_recurso=tipo_recurso)
        else:
            return qs.none()
        if self.q:
            qs = qs.filter(nombre_recurso__icontains=self.q)

        return qs
