from django.shortcuts import render
from rest_framework import viewsets
from .models import Museu
from .serializer import MuseuSerializer
# Create your views here.


class MuseuViewSet(viewsets.ModelViewSet):
    queryset = Museu.objects.all()
    serializer_class = MuseuSerializer
