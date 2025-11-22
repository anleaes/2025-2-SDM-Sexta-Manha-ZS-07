from django.shortcuts import render
from rest_framework import viewsets
from .models import Obra
from .serializer import ObraSerializer
# Create your views here.
class ObraViewSet(viewsets.ModelViewSet):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer
