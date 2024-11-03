from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from solicitud import views 

router=routers.DefaultRouter()


router.register(r'solicitud',views.SolicitudView,'solicitud')
urlpatterns=[
    path("api/v1/",include(router.urls)),
   
]

