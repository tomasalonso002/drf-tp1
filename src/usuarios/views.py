from rest_framework import status, viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import Group
from django.utils import timezone

from django.contrib.auth.models import Group

from .permissions import PermissionsJefe, PermissionAlumno, PermissionEmpleado
from .models import UsuarioPersonalizado
from .serializers import UsuarioPublicSerializer,UsuarioSerializer
# Create your views here.


#Admin

#Create User
class UserViewSets(viewsets.ModelViewSet):
    queryset = UsuarioPersonalizado.objects.filter(is_active=True)
    serializer_class = UsuarioSerializer
    permission_classes=[PermissionsJefe]

   
    @action(detail=True, methods=['post'])
    def eliminado_logico(self, request, pk=None):
        usuario = self.get_object()
        timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
        usuario.is_active = False
        usuario.username = f'eliminado-{usuario.username}-{timestamp}'
        usuario.email = f'eliminado-{usuario.email}-{timestamp}'
        usuario.dni = f'eliminado-{usuario.dni}-{timestamp}'
        usuario.save()
        return Response(
                    {'detail': 'El usuario se elimino correctamente'},
                    status=status.HTTP_200_OK
                )
#GET Alumno
class UserAlumnoGetViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = UsuarioPersonalizado.objects.filter(is_active = True, groups__name = 'Alumno' )
    serializer_class = UsuarioPublicSerializer
    permission_classes=[PermissionEmpleado]

#GET Empleado
class UserEmpleadoGetViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = UsuarioPersonalizado.objects.filter(is_active = True, groups__name = 'Empleado' )
    serializer_class = UsuarioPublicSerializer
    permission_classes=[PermissionsJefe]

#GET Jefe
class UserJefeGetViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = UsuarioPersonalizado.objects.filter(is_active = True, groups__name = 'Jefe' )
    serializer_class = UsuarioPublicSerializer
    permission_classes=[PermissionsJefe]


    



