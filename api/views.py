from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
#from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuarios,Departamento,Casilla,AlquilerCasillas
from .serializers import UsuariosSerializer,DepartamentoSerializer,CasillaSerializer ,AlquilerCasillasSerializer
from .filters import CasillaFilter
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset=Usuarios.objects.all()
    serializer_class=UsuariosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']
class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset=Departamento.objects.all()
    serializer_class=DepartamentoSerializer
class CasillasViewSet(viewsets.ModelViewSet):
    queryset=Casilla.objects.all()
    serializer_class=CasillaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = CasillaFilter
    ordering_fields = ['num_Casilla']
    ordering = ['num_Casilla']
class AlquilerCasillasViewSet(viewsets.ModelViewSet):
    queryset=AlquilerCasillas.objects.all()
    serializer_class=AlquilerCasillasSerializer
    