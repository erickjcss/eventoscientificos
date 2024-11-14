from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from personas.models import Personas
# Create your models here.


class Publications(models.Model):
    publicacionesPer = models.ForeignKey(Personas, on_delete=models.CASCADE)
    nombreEvento=models.CharField(max_length=50)
    lugar=models.CharField(max_length=50)
    fechaEvento=models.DateField()
    fechaFinEvento=models.DateField(blank=True,default='2024-03-29')
    limiteEntrega= models.DateField()
    emailEvento=models.EmailField()
    enlace=models.URLField()
    tematicas=models.TextField()
    pdf = models.FileField(upload_to="imagenes",blank=True)
    foto = models.ImageField(upload_to="imagenes",blank=True)  
    likes=models.TextField(blank=True,default="")
    aprobada=models.BooleanField(blank=True,default=True)

   
    def __str__(self):
       return self.nombreEvento
    

