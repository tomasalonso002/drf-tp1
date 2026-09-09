from rest_framework import serializers

from .models import UsuarioPersonalizado

class UsuarioPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPersonalizado
        fields = [
            'username',
            'first_name',
            'last_name',
            'telefono',
            'dni',
            'email',
            'fecha_nacimiento'
        ]
        read_only_fields=['first_name','last_name', 'dni', 'fecha_nacimiento']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPersonalizado
        fields = '__all__'
        read_only_fields=['id','last_login', 'is_superuser', 'is_staff', 'date_joined', 'groups','user_permissions']

