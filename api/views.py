#from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Usuarios,Departamento,Casilla,AlquilerCasillas
from .serializers import UsuariosSerializer,DepartamentoSerializer,CasillaSerializer ,AlquilerCasillasSerializer
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset=Usuarios.objects.all()
    serializer_class=UsuariosSerializer
class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset=Departamento.objects.all()
    serializer_class=DepartamentoSerializer
class CasillasViewSet(viewsets.ModelViewSet):
    queryset=Casilla.objects.all()
    serializer_class=CasillaSerializer
class AlquilerCasillasViewSet(viewsets.ModelViewSet):
    queryset=AlquilerCasillas.objects.all()
    serializer_class=AlquilerCasillasSerializer