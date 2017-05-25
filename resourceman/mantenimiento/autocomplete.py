from dal import autocomplete
from tipos_recursos.models import Recurso
from .models import Mantenimiento


class MantenimientoByTipoRecursoAutocomplete(autocomplete.Select2QuerySetView):
    """
    Clase para filtrar los recursos que no estan en mantenimiento
    por tipos de recursos
    """
    def get_queryset(self):
        """
        Obtiene una lista de los recursos que no estan en mantenimiento ni fuera de uso
        a partir del tipo de recurso seleccionado
        :return: 
        """
        if not self.request.user.is_authenticated():
            return Mantenimiento.objects.none()

        tipo_recurso = self.forwarded.get('tipo_recurso', None)
        recurso = Recurso.objects.all().filter(tipo_recurso=tipo_recurso).exclude(estado__codigo="MAN"
                                                ).exclude(estado__codigo="FUS"
                                                          ).order_by('nombre_recurso')

        if tipo_recurso:
            recurso.filter(tipo_recurso=tipo_recurso)
        else:
            recurso.none()

        if self.q:
            recurso = recurso.filter(nombre_recurso__icontains=self.q)
        return recurso
