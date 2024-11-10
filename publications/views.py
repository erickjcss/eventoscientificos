from rest_framework import viewsets
from .serializer import PublicationsSerializer
from .models import Publications
from django.shortcuts import render
from rest_framework.views import APIView
class PublicationsView(viewsets.ModelViewSet):
    serializer_class=PublicationsSerializer
    queryset=Publications.objects.all()