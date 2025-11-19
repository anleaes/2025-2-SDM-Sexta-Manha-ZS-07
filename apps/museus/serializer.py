from .models import Museu
from rest_framework import serializers

class MuseuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Museu
        fields = '__all__'