from rest_framework import viewsets
from .serializer import SolicitudSerializer
from .models import Solicitud


class SolicitudView(viewsets.ModelViewSet):
    serializer_class=SolicitudSerializer
    queryset=Solicitud.objects.all()