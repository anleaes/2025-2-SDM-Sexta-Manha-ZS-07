from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'reservas'

router = routers.DefaultRouter()
<<<<<<< HEAD
router.register('', views.ReservaViewSet, basename='reservas')
=======
router.register('', views.ReservaViewset, basename='reservas')
>>>>>>> origin/main

urlpatterns = [
    path('', include(router.urls) )
]