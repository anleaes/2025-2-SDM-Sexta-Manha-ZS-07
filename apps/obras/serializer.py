from .models import Obra
from rest_framework import serializers

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = '__all__'