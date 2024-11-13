from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from publications import views 

router=routers.DefaultRouter()


router.register(r'publications',views.PublicationsView,'publications')
urlpatterns=[
    path("api/v1/",include(router.urls)),
   
]

