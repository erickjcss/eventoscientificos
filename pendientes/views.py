from rest_framework import viewsets
from .serializer import PendientesSerializer
from .models import Pendientes
import json


class PendientesView(viewsets.ModelViewSet):
    serializer_class=PendientesSerializer
    queryset=Pendientes.objects.all()

    
