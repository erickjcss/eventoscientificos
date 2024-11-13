from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password','email', 'first_name', 'last_name']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()    

class CambiarContrasenaSerializer(serializers.Serializer):
    username = serializers.CharField()
    contrasena_actual = serializers.CharField()
    contrasena_nueva = serializers.CharField()

class LogInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
class CheckSerializer(serializers.Serializer):
    password = serializers.CharField()
    newpassword = serializers.CharField()

class CrearContrasenaSerializer(serializers.Serializer):
    password = serializers.CharField()
    
class EliSerializer(serializers.Serializer):
    username=serializers.CharField()