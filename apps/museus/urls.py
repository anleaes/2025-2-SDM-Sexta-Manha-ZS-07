from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'museus'

router = routers.DefaultRouter()
router.register('', views.MuseuViewSet, basename='museus')

urlpatterns = [
    path('', include(router.urls) )
]