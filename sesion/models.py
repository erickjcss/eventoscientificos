from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from personas.models import Personas
# Create your models here.


class Sesion(models.Model):
    fechaInicio=models.DateField()
    fechaCierre=models.DateField(blank=True)
    horaInicio=models.TimeField()
    horaCierre=models.TimeField(blank=True)
    email=models.EmailField()
    idPer=models.ForeignKey(Personas, on_delete=models.SET_NULL, null=True)

   
    def __str__(self):
       return self.fechaInicio