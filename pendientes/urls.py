from django.urls import path,include

from rest_framework import routers
from pendientes import views 


router=routers.DefaultRouter()


router.register(r'pendientes',views.PendientesView,'pendientes')
urlpatterns=[
    path("api/v1/",include(router.urls)),

    
]