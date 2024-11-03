from rest_framework import viewsets
from .serializer import NotificaSerializer
from .models import Notifica
import json
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

class NotificaView(viewsets.ModelViewSet):
    serializer_class=NotificaSerializer
    queryset=Notifica.objects.all()

    