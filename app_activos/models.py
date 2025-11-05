from django.db import models

class Activo(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
