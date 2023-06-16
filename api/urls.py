from django.urls import path
from .views import UsuariosViewSet,DepartamentoViewSet,CasillasViewSet ,AlquilerCasillasViewSet
from rest_framework.authtoken import views
urlpatterns = [
    path('usuarios/',UsuariosViewSet.as_view({'get':'list'})),
    path('Register/',UsuariosViewSet.as_view({'post':'create','get':'list'})),
    path('departamento/',DepartamentoViewSet.as_view({'get':'list'})),
    path('casillas/',CasillasViewSet.as_view({'get':'list','post':'create'})), 
    path('alqcasillas/',AlquilerCasillasViewSet.as_view({'get':'list','post':'create'})),
    path('login/',views.obtain_auth_token),
]