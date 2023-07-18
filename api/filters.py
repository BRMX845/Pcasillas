import django_filters
from .models import Casilla,Departamento

class CasillaFilter(django_filters.FilterSet):
    departamento__nombre = django_filters.CharFilter(lookup_expr='icontains', field_name='departamento__nombre')

    class Meta:
        model = Casilla
        fields = ['departamento__nombre']
