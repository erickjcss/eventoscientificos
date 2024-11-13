from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from personas.models import Personas
# Create your models here.


class Sesi(models.Model):
    fecha=models.DateField()
    hora=models.TimeField()
    accion=models.TextField()
    email=models.EmailField()
    
   
    def __str__(self):
       return self.accion