from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.
from publications.models import Publications
class Likes(models.Model):
    pubLikes= models.ForeignKey(Publications, on_delete=models.CASCADE)
    cantLikes=models.ImageField(blank=True,default=0)
    