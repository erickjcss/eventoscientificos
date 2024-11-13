from rest_framework import viewsets
from .serializer import LikesSerializer
from .models import Likes
import json
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

class LikesView(viewsets.ModelViewSet):
    serializer_class=LikesSerializer
    queryset=Likes.objects.all()

    