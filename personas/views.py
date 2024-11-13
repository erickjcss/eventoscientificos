from rest_framework import viewsets
from .serializer import PersonasSerializer
from .models import Personas
import json
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

class PersonasView(viewsets.ModelViewSet):
    serializer_class=PersonasSerializer
    queryset=Personas.objects.all()

    



# Vista que obtiene el nombre de usuario activo
@login_required
def usuario_activo(request):
    # Si el usuario está autenticado, puedes obtener su nombre de usuario de la sesión
    nombre_usuario = "ja"
    
    return JsonResponse({'nombre': nombre_usuario})
    