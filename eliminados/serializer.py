from rest_framework import serializers
from .models import Eliminados
class EliminadosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Eliminados
        fields='__all__'
    