from rest_framework import serializers
from .models import Rutina, RutinaPersonalizada
from usuarios.serializers import UsuarioPublicSerializer

class RutinaGETSerializers(serializers.ModelSerializer):
    usuario_activo = UsuarioPublicSerializer(read_only=True)
    class Meta:
        model = Rutina
        fields=[
            'id',
            'name',
            'archivo',
            'fecha_at',
            'is_active',
            'usuario_activo'
        ]
        read_only_fields=['id','is_active', 'fecha_at']

class RutinaPOSTSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields=[
            'id',
            'name',
            'archivo',
            'fecha_at',
            'is_active',
            'usuario_activo'
        ]
        read_only_fields=['id','is_active', 'fecha_at']

class RutinaPerosnalizadaPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = RutinaPersonalizada
        fields =[
            'id',
            'name',
            'archivo',
            'alumno',
            'fecha_at',
            'is_active',
            'usuario_activo'
        ]
        read_only_fields=['id','fecha_at','is_active']

class RutinaPerosnalizadaGETSerializer(serializers.ModelSerializer):
    alumno = UsuarioPublicSerializer(read_only=True)
    usuario_activo = UsuarioPublicSerializer(read_only=True)
    class Meta:
        model = RutinaPersonalizada
        fields =[
            'id',
            'name',
            'archivo',
            'alumno',
            'fecha_at',
            'is_active',
            'usuario_activo'
        ]
        read_only_fields=['id','fecha_at','is_active']