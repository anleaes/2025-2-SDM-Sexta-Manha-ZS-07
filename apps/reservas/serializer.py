from .models import Reserva
from rest_framework import serializers

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
<<<<<<< HEAD
        fields = '__all__'
        
=======
        fields = '__all__'
>>>>>>> origin/main
