from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'galerias'

router = routers.DefaultRouter()
router.register('', views.GaleriaViewSet, basename='galerias')

urlpatterns = [
    path('', include(router.urls) )
]