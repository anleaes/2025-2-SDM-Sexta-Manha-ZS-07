from .models import Reserva
from rest_framework import serializers

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'