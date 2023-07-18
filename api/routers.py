from rest_framework.routers import DefaultRouter
from .views import UsuariosViewSet ,AlquilerCasillasViewSet,CasillasViewSet,DepartamentoViewSet
router=DefaultRouter()
router.register(r'usuario',UsuariosViewSet)
router.register(r'alquiler',AlquilerCasillasViewSet)
router.register(r'casillas',CasillasViewSet)
router.register(r'departamento',DepartamentoViewSet)
urlpatterns=router.urls