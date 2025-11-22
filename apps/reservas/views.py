from django.shortcuts import render
from rest_framework import viewsets
from .models import Reserva
from .serializer import ReservaSerializer
# Create your views here.

<<<<<<< HEAD
class ReservaViewSet(viewsets.ModelViewSet):
=======

class ReservaViewset(viewsets.ModelViewSet):
>>>>>>> origin/main
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
