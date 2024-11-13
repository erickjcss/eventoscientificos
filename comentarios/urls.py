from django.urls import path,include

from rest_framework import routers
from comentarios import views 


router=routers.DefaultRouter()


router.register(r'comentarios',views.ComentariosView,'comentarios')
urlpatterns=[
    path("api/v1/",include(router.urls)),
    
    
]

