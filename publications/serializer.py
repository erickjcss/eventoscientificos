from rest_framework import serializers,status
from rest_framework.response import Response
from .models import Publications

class PublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publications
        fields='__all__'
        def get_photo_url(self,obj):
            request=self.context.get('request')
            photo_url=obj.fingerprint.url
            return request.build_absolute_uri(photo_url)