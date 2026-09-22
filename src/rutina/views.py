from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import RutinaGETSerializers, RutinaPOSTSerializers , RutinaPersonalizadaGETSerializer, RutinaPersonalizadaPOSTSerializer
from .models import Rutina, RutinaPersonalizada
from usuarios.permissions import PermissionAlumno, PermissionEmpleado,PermissionsJefe
#Rutina 
class RutinaViewSets(viewsets.ModelViewSet):
    queryset = Rutina.objects.filter(is_active=True).select_related('usuario_activo')
    permission_classes=[PermissionEmpleado]
    def get_serializer_class(self):
        if self.request.method=='GET':
            return RutinaGETSerializers
        else:
            return RutinaPOSTSerializers

    @action(detail=True, methods=['post'])
    def eliminado_logico(self, request, pk:None):
        rutina = self.get_object()
        rutina.is_active = False
        rutina.save()
        return Response({'mensaje':'Rutina borrada correctamente'}, status=status.HTTP_200_OK)
    
#GET Rutina
class RutinaGetViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = Rutina.objects.filter(is_active = True).select_related('usuario_activo')
    serializer_class = RutinaGETSerializers
    permission_classes=[PermissionEmpleado]

#RutinaPersonalizada
class RutinaPersonalizadaViewSets(viewsets.ModelViewSet):
    queryset = RutinaPersonalizada.objects.filter(is_active=True).select_related('usuario_activo', 'alumno')
    permission_classes=[PermissionEmpleado]
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RutinaPersonalizadaGETSerializer
        else:
            return RutinaPersonalizadaPOSTSerializer

    @action(detail=True, methods=['post'])
    def eliminado_logico(self, request, pk:None):
        rutina = self.get_object()
        rutina.is_active = False
        rutina.save()
        return Response({'mensaje':'Rutina Personalizada borrada correctamente'}, status=status.HTTP_200_OK)


#GET RutinaPersonalizada
class RutinaPersonalizadaGetViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = RutinaPersonalizada.objects.filter(is_active = True).select_related('usuario_activo')
    serializer_class = RutinaPersonalizadaGETSerializer
    permission_classes = [PermissionAlumno]
