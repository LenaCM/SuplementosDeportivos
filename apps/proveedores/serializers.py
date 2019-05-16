from rest_framework import serializers
from .models import Proveedor

class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = [
            'pk','nombre', 'mail','comentario',
        ]