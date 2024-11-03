from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UsuariosSerializer
from .models import Usuarios
from django.http import JsonResponse
import base64

class UsuariosView(viewsets.ModelViewSet):
    serializer_class=UsuariosSerializer
    queryset=Usuarios.objects.all()
# Create your views here.


def mi_vista(request):
    datos = Usuarios.objects.all().values('id', 'pdf')
    for dato in datos:
        pdf_bytes = dato['pdf'].read()
        pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
        dato['pdf'] = pdf_base64
    return JsonResponse(list(datos), safe=False)