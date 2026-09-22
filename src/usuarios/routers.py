from rest_framework.routers import DefaultRouter
from .views import UserViewSets,UserEmpleadoGetViewSets,UserJefeGetViewSets,UserAlumnoGetViewSets
router = DefaultRouter()
router.register('empleado-get', UserEmpleadoGetViewSets, basename='user-empleado-get-api')
router.register('jefe-get', UserJefeGetViewSets, basename='user-jefe-get-api')
router.register('alumno-get', UserAlumnoGetViewSets, basename='user-alumno-get-api')
router.register('', UserViewSets,basename='user-empleado-api')




