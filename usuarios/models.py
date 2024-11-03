from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from personas.models import Personas
# Create your models here.


class Usuarios(models.Model):
    
    pdf = models.FileField(upload_to='pdfs/')
  
   
    def __str__(self):
       return self.nombreEvento