from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from personas import views 


router=routers.DefaultRouter()


router.register(r'personas',views.PersonasView,'personas')
urlpatterns=[
    path("api/v1/",include(router.urls)),
    path("docs/",include_docs_urls(title="Personas API")),
    
]