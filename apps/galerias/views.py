from django.shortcuts import render
from rest_framework import viewsets
from .models import Galeria
from .serializer import GaleriaSerializer
# Create your views here.
<<<<<<< HEAD
class GaleriaViewSet(viewsets.ModelViewSet):
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer
=======

class GaleriaViewSet(viewsets.ModelViewSet):
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer
>>>>>>> origin/main
