from rest_framework.serializers import ModelSerializer
from proveedores.models import Proveedor

class ProveedorSerializer(ModelSerializer):
    class Meta:
        model = Proveedor
        fields = [
            'pk','nombre','mail','comentario',
        ]
        read_only_fields = ['pk']