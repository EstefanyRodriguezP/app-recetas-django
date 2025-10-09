from django.db import models

# Create your models here.
class Receta(models.Model):
    nombre = models.CharField(max_length=200)
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    imagen = models.ImageField(upload_to='recetas/') # Guarda en /media/recetas/

    def __str__(self):
        return self.nombre
    
class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre} ({self.email})"