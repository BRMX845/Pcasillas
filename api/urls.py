from django.urls import path
from .views import UsuariosViewSet,DepartamentoViewSet,CasillasViewSet ,AlquilerCasillasViewSet
urlpatterns = [
    path('usuarios/',UsuariosViewSet.as_view({'get':'list'})),
    path('Register/',UsuariosViewSet.as_view({'post':'create'})),
    path('departamento/',DepartamentoViewSet.as_view({'get':'list'})),
    path('casillas/',CasillasViewSet.as_view({'get':'list','post':'create'})), 
    path('alqcasillas/',AlquilerCasillasViewSet.as_view({'get':'list','post':'create'})),
]