from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.hashers import make_password
from publications.models import Publications

class Comentarios(models.Model):
    comPub=models.ForeignKey(Publications, on_delete=models.CASCADE)
    emailPer=models.CharField(blank=True,default='invitado',max_length=100)
    fechaPub=models.DateField()
    horaPub=models.TimeField()
    contenido=models.TextField(default='',blank=True)


