from rest_framework import viewsets
from .serializer import ComentariosSerializer
from .models import Comentarios
import json
from django.http import HttpResponse, JsonResponse


class ComentariosView(viewsets.ModelViewSet):
    serializer_class=ComentariosSerializer
    queryset=Comentarios.objects.all()

    

