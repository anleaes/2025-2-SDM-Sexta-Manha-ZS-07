from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'catalogos'

router = routers.DefaultRouter()
<<<<<<< HEAD
router.register('', views.CatalogoViewSet, basename='catalogos')
=======
router.register('', views.CatalogoViewsSet, basename='catalogos')
>>>>>>> origin/main

urlpatterns = [
    path('', include(router.urls) )
]