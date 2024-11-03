from django.db import models

from personas.models import Personas
# Create your models here.
class Notifica(models.Model):
    notificacionesPer = models.ForeignKey(Personas, on_delete=models.CASCADE)
    title=models.TextField()
    contenido=models.TextField()
    resumen=models.TextField()
    fechaNot=models.DateField()
    horaNot=models.TimeField()
    def __str__(self):
       return self.title