from rest_framework import serializers
from .models import Notifica
class NotificaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notifica
        fields='__all__'
    