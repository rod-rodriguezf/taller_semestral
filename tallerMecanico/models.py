from django.db import models

# Create your models here.
class Repuestos(models.Model):
    nombre_repuesto = models.CharField(primary_key=True, max_length=25)
    precio_producto = models.IntegerField()
    descripcion_producto = models.TextField()

    def __str__(self):
        return self.nombre_repuesto