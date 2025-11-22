<<<<<<< HEAD
=======

>>>>>>> origin/main
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'obras'

router = routers.DefaultRouter()
router.register('', views.ObraViewSet, basename='obras')

urlpatterns = [
    path('', include(router.urls) )
]