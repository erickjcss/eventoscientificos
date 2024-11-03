from rest_framework import serializers
from .models import Publications
class PublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publications
        fields='__all__'
    