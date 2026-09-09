from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.utils import timezone


from .models import UsuarioPersonalizado
from .serializers import UsuarioPublicSerializer,UsuarioSerializer
# Create your views here.

#Admin


class UserListCreateView(generics.ListCreateAPIView):
    queryset= UsuarioPersonalizado.objects.filter(is_active=True)
    serializer_class = UsuarioSerializer


class UserRetrivUpdateView(generics.RetrieveUpdateAPIView):
    queryset=UsuarioPersonalizado.objects.all()
    serializer_class= UsuarioPublicSerializer


class UsuarioSoftDeleteView(generics.DestroyAPIView):
    queryset=UsuarioPersonalizado.objects.filter(is_active=True)
    serializer_class = UsuarioPersonalizado

    def destroy(self, request, *args,**kwargs):
        instance = self.get_object()
        
        timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
        instance.is_active = False
        instance.username = f'eliminado-{instance.username}-{timestamp}',
        instance.email = f'eliminado-{instance.email}-{timestamp}'
        instance.dni = f'eliminado-{instance.dni}-{timestamp}'

        instance.save()
        return Response(
            {'detail': 'El usuario se elimino correctamente'},
            status=status.HTTP_200_OK
        )

#Employee


#User

