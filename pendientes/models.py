from django.db import models
from personas.models import Personas
# Create your models here.
class Pendientes(models.Model):
    publicacionesPer = models.ForeignKey(Personas, on_delete=models.CASCADE)
    nombreEvento=models.CharField(max_length=50)
    lugar=models.CharField(max_length=50)
    fechaEvento=models.DateField()
    limiteEntrega= models.DateField()
    emailEvento=models.EmailField()
    enlace=models.URLField()
    tematicas=models.TextField()
    pdf = models.FileField(upload_to='pdfs/',blank=True)
    foto = models.ImageField(upload_to='pdfs/',blank=True)  
    likes=models.TextField(blank=True)

   
    def __str__(self):
       return self.nombreEvento