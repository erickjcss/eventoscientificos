from rest_framework import viewsets
from .serializer import SesionSerializer
from .models import Sesion


class SesionView(viewsets.ModelViewSet):
    serializer_class=SesionSerializer
    queryset=Sesion.objects.all()