from rest_framework import serializers
from .models import Sesi
class SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sesi
        fields='__all__'
    