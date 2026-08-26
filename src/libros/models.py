from django.db import models

# Create your models here.

class Libros(models.Model):
    titulo = models.CharField(max_length=40)
    escritor = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    def __str__(self):
        return self.titulo
    
    