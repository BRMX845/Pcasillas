import django_filters
from .models import Casilla

class CasillaFilter(django_filters.FilterSet):
    departamento = django_filters.CharFilter(field_name='departamento__nombre', lookup_expr='exact')

    class Meta:
        model = Casilla
        fields = ['departamento']
