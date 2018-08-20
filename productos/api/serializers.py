from rest_framework import serializers
from productos.models import Producto

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Producto
        fields = (
            'nombre',
            'descripcion',
            'stock',
            'stock_minimo',
            'costo',
            'precio_minorista',
            'precio_mayorista',
        )