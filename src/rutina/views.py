from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status, mixins
from .serializers import RutinaGETSerializers, RutinaPOSTSerializers , RutinaPerosnalizadaGETSerializer, RutinaPerosnalizadaPOSTSerializer
from .models import Rutina, RutinaPersonalizada
# Create your views here.

class RutinaListCreateView(
    generics.ListCreateAPIView):
    queryset = Rutina.objects.filter(is_active=True).select_related('usuario_activo')
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RutinaGETSerializers
        else:
            return RutinaPOSTSerializers


class RutinaDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rutina.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RutinaGETSerializers
        else:
            return RutinaPOSTSerializers
    def destroy(self, request, *args, **kwargs):
        instance =self.get_object()
        instance.is_active = False
        instance.save()
        return Response(
            {'mensaje':'Se borro correctamente la rutina'},
            status=status.HTTP_200_OK
        )


class RutinaPersonalizadaListCreateView(generics.ListCreateAPIView):
    queryset = RutinaPersonalizada.objects.filter(is_active=True).select_related('usuario_activo','alumno')
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return  RutinaPerosnalizadaGETSerializer
        else:
            return RutinaPerosnalizadaPOSTSerializer



class RutinaPersonalizadaDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RutinaPersonalizada.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RutinaPerosnalizadaGETSerializer
        else:
            return RutinaPerosnalizadaPOSTSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(
            {'mensaje': 'Se borro correctamente la rutina'},
            status=status.HTTP_200_OK
        )


