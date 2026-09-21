from rest_framework import serializers
from django.contrib.auth.models import Group
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
            'fecha_nacimiento',
            'password',
            'rol',
            'groups'
        ]
        read_only_fields=['first_name','last_name', 'dni', 'fecha_nacimiento']



class UsuarioSerializer(serializers.ModelSerializer):

    rol = serializers.ChoiceField(
        choices=['Alumono','Empleado','Jefe'],
        write_only = True
    )

    class Meta:
        model = UsuarioPersonalizado
        fields = ['id', 'username','last_name','first_name','password','telefono','email','dni','rol']
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):
            rol = validated_data.pop('rol')

            usuario = UsuarioPersonalizado.objects.create_user(
                **validated_data
            )

            grupo = Group.objects.get(name=rol)
            usuario.groups.add(grupo)

            return usuario


        
