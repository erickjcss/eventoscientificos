from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from usuarios import views 

router=routers.DefaultRouter()


router.register(r'usuarios',views.UsuariosView,'usuarios')
urlpatterns=[
    path("api/v1/",include(router.urls)),
   
]