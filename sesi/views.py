from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import SesionSerializer
from .models import Sesi


class SesionView(viewsets.ModelViewSet):
    serializer_class=SesionSerializer
    queryset=Sesi.objects.all()