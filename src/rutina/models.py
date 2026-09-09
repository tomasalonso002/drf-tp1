from django.db import models
from usuarios.models import UsuarioPersonalizado
# Create your models here.

class Rutina(models.Model):
    name = models.CharField(max_length=40)
    archivo = models.CharField(max_length=259)
    fecha_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    usuario_activo = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE, related_name='rutina', null=True, blank=True)
    def __str__(self):
        return f'{self.name}-{self.fecha_at}'

class RutinaPersonalizada(models.Model):    
    name = models.CharField(max_length=40)
    archivo = models.CharField(max_length=259)
    alumno = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE, related_name='rutinas_alumno')
    fecha_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    usuario_activo = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE, related_name='rutina_usuario_activo', null=True, blank=True)
    def __str__(self):
        return f'{self.name}-{self.fecha_at}'
  