from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'descripcion',
            'stock',
            'stock_minimo',
            'costo',
            'precio_minorista',
            'precio_mayorista',
        ]
        read_only_fields = ['pk']

#esta clase convierte a json y ademas valida  
# ejemplo de validacion min 21.33      