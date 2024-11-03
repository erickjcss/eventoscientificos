from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from sesi import views 

router=routers.DefaultRouter()


router.register(r'sesi',views.SesionView,'sesi')
urlpatterns=[
    path("api/v1/",include(router.urls)),
   
]

