from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'artistas'
router = routers.DefaultRouter()
router.register('', views.ArtistaViewSet, basename='artistas')

urlpatterns = [
    path('', include(router.urls) )
]