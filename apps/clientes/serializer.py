<<<<<<< HEAD

=======
>>>>>>> origin/main
from .models import Cliente
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
<<<<<<< HEAD
        fields = '__all__'
        
=======
        fields = '__all__'
>>>>>>> origin/main
