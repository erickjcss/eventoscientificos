from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from us import views 
from .views import LoginView,CambiarContrasenaView,LogInView,UserActive,CrearContrasenaView,EliminarUser,EliminarAdmin
router=routers.DefaultRouter()


router.register(r'us',views.UserViewSet,'us')
urlpatterns=[
    path("api/v1/",include(router.urls)),
     path('api/v1/usuario_activo/', UserActive.as_view(), name='usuario_activo'),
     path('api/v1/iniciar_sesion/', LogInView.as_view(), name='iniciar_sesion'),
     path('api/v1/login/', LoginView.as_view(), name='login'),
     path('api/v1/cambiar_contr/', CambiarContrasenaView.as_view(), name='cambiar_contr'),
     path('api/v1/crear_contr/', CrearContrasenaView.as_view(), name='crear_contr'),
     path('api/v1/eliminar/', EliminarUser.as_view(), name='eliminar_user'),
     path('api/v1/elAdm/', EliminarAdmin.as_view(), name='eliminar_admin'),
]

