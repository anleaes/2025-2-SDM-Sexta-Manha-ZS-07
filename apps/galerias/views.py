from django.shortcuts import render
from rest_framework import viewsets
from .models import Galeria
from .serializer import GaleriaSerializer
# Create your views here.
class GaleriaViewSet(viewsets.ModelViewSet):
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer
