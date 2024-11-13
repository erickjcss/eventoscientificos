from django.contrib.auth.models import User 
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UserSerializer
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login
from .serializers import LoginSerializer,CambiarContrasenaSerializer,LogInSerializer,CheckSerializer,CrearContrasenaSerializer,EliSerializer
from rest_framework import permissions,status
from django.views.decorators.csrf import csrf_exempt
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs): 
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True) 
        user = serializer.save() # Guarda el usuario creado 
        token = Token.objects.create(user=user) # Crea un token para el usuario 
        self.perform_create(serializer) 
        headers = self.get_success_headers(serializer.data) 
        return Response({ 
        'user': serializer.data, 
        'token': token.key # Devuelve el token en la respuesta 
    }, status=status.HTTP_201_CREATED, headers=headers) 



    
    
    
class LoginView(APIView):
    permission_classes=(permissions.AllowAny,)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username)
            if user.check_password(password) is not None:
                try:
                    token = Token.objects.get(user=user)
                    return Response({'token': token.key})
                except Token.DoesNotExist:
                    return Response({'error': 'Token no encontrado'}, status=status.HTTP_404_NOT_FOUND) 
                
            else:
                # Credenciales inválidas
                return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # Datos de entrada inválidos
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class ComprobarContrasenView(APIView):
    def post(self,request):
        serializer=CheckSerializer(data=request.data)
        if serializer.is_valid():
            password=serializer.validated_data['password']
            newpassword=serializer.validated_data['newpassword']
            password=make_password(password)
            newpassword=make_password(newpassword)
            if password==newpassword:
                 return Response({'mensaje': 'Las contraseñas coinciden.'}, status=status.HTTP_200_OK)
            else:
                  return Response({'error': 'La contraseña actual no coincide.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
class CrearContrasenaView(APIView):
    def post(self, request):
        serializer = CrearContrasenaSerializer(data=request.data)   
        if serializer.is_valid():
            password=serializer.validated_data['password']
            password=make_password(password)     
            return Response({'password': password}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Algo falló.'}, status=status.HTTP_404_NOT_FOUND)
class CambiarContrasenaView(APIView):
    def put(self, request):
        serializer = CambiarContrasenaSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            contrasena_actual = serializer.validated_data['contrasena_actual']
            contrasena_nueva = serializer.validated_data['contrasena_nueva']

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

            if user.check_password(contrasena_actual):
                contrasena_encriptada_nueva = make_password(contrasena_nueva)
                user.set_password(contrasena_nueva)
                user.save()
                return Response({'password':contrasena_encriptada_nueva,'mensaje': 'Contraseña cambiada exitosamente.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'La contraseña actual no coincide.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            

class LogInView(APIView):
    def post(self, request):
        serializer = LogInSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

            if user.check_password(password):
                user = authenticate(request, username=username, password=password)
                login(request, user)
                token = Token.objects.get(user=user)
                return Response({'token': token.key,'username': username}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Usuario y contraseña inválidos'}, status=status.HTTP_404_NOT_FOUND)
    
        return JsonResponse({'nombre': 'ja'})
                        
            
                
        
class UserActive(APIView):
     
    def post(self,request):
   
        nombre_usuario = "ja"
    
        return JsonResponse({'nombre': nombre_usuario})


class EliminarUser(APIView):    
    def post(self,request):
        serializer = LogInSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
            if user.check_password(password):
                user = authenticate(request, username=username, password=password)
            
                user.delete()
        
          
                return HttpResponse('Usuario eliminado .')
            else:
                return HttpResponse('Credenciales Inválidas.')

    
        return HttpResponse('No has enviado una solicitud POST .')
    
class EliminarAdmin(APIView):    
    def post(self,request):
        serializer = EliSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
            if user is not None:
                
            
                user.delete()
        
          
                return HttpResponse('Usuario eliminado .')
            else:
                return HttpResponse('Credenciales Inválidas.')

    
        return HttpResponse('No has enviado una solicitud POST .')    