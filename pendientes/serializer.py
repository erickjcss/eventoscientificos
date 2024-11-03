from rest_framework import serializers
from .models import Pendientes
class PendientesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pendientes
        fields='__all__'
    