from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'catalogos'

router = routers.DefaultRouter()
router.register('', views.CatalogoViewsSet, basename='catalogos')

urlpatterns = [
    path('', include(router.urls) )
]