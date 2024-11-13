from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.hashers import make_password
# Create your models here.


class Personas(models.Model):
    nombrePer=models.CharField(max_length=20)
    apellidos=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    cantNotificaciones=models.IntegerField(blank=True,default=0)
    contr= models.CharField(
        max_length=100,
        )
    esTrabajador=models.BooleanField(default=True)
    catdoc=models.CharField(max_length=50,blank=True)
    equivocaciones=models.IntegerField(blank=True,default=0)
    uso=models.IntegerField(blank=True,default=0)
    def __str__(self):
       
       return self.nombrePer+' '+self.apellidos
    """ def save(self, *args, **kwargs):
        # Antes de guardar, encriptamos la contraseña si es nueva o se ha modificado
        if self._state.adding or 'contr' in self.get_deferred_fields():
            self.contr = make_password(self.contr)
        super(Personas, self).save(*args, **kwargs)     """
        