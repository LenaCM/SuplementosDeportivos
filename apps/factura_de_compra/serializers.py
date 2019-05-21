from rest_framework import serializers
from .models import facturaCompra, facturaCompraContieneProductos

class facturaCompraSerializer(serializers.ModelSerializer):

    class Meta:
        model = facturaCompra
        fields = [
            'pk', 'fecha', 'total', 'idProveedor'
        ]
        extra_kwargs = {'fecha':{'required':True}}
        depth = 1

class facturaCompraContieneProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = facturaCompraContieneProductos
        fields = [
            'idProducto', 'precio', 'cantidad', 'descuento', 'idFacturaCompra'
        ]
        