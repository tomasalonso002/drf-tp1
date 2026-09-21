from rest_framework.routers import DefaultRouter
from .views import UserEmpleadoViewSets, UserEmpleadoGetViewSets
router = DefaultRouter()
router.register('empleado', UserEmpleadoViewSets,basename='user-empleado-api')
router.register('empleado-get', UserEmpleadoGetViewSets, basename='user-empleado-get-api')