from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import RutinaGETSerializers, RutinaPOSTSerializers , RutinaPerosnalizadaGETSerializer, RutinaPersonalizadaPOSTSerializer
from .models import Rutina, RutinaPersonalizada

class RutinaViewSets(viewsets.ModelViewSet):
    queryset = Rutina.objects.filter(is_active=True).select_related('usuario_activo')
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

class RutinaPersonalizadaViewSets(viewsets.ModelViewSet):
    queryset = RutinaPersonalizada.objects.filter(is_active=True).select_related('usuario_activo', 'alumno')
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RutinaPerosnalizadaGETSerializer
        else:
            return RutinaPersonalizadaPOSTSerializer

    @action(detail=True, methods=['post'])
    def eliminado_logico(self, request, pk:None):
        rutina = self.get_object()
        rutina.is_active = False
        rutina.save()
        return Response({'mensaje':'Rutina Personalizada borrada correctamente'}, status=status.HTTP_200_OK)
    
