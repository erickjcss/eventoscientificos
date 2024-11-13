from django.db import models

from publications.models import Publications

class Solicitud(models.Model):
    solPub=models.ForeignKey(Publications, on_delete=models.CASCADE)
    emailPer=models.EmailField()
    pdf=models.FileField(upload_to='pdfs/',blank=True)
    modalidad=models.CharField(max_length=20)


    def __str__(self):
       return self.emailPer