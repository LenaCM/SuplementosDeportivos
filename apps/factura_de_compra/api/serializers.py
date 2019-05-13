from django.shortcuts import render
from django.db import models
from rest_framework import serializers

from apps.proveedores.models import Proveedor
from apps.productos.models import Producto
from apps.factura_de_compra.models import (
    facturaCompra,
    facturaCompraContieneProductos
)

#----------------------------------------------------------------------------------
class FacturaCompraSerializer(serializers.Serializer):
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE, verbose_name="proveedor" )
    class Meta:
        model = facturaCompra
        fields = [
            'id_factura_compra',
            'id_proveedor',
            'fecha',
            'total',
        ]
        read_only_fields = ['id_proveedor','id_factura_compra']

#----------------------------------------------------------------------------------
class facturaCompraContieneProductosSerializer(serializers.ModelSerializer):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="producto")
    factura_compra = models.ForeignKey(facturaCompra, on_delete=models.CASCADE, verbose_name="factura Compra")
    class Meta:
        model = facturaCompraContieneProductos
        fields = [
            'id_producto',
            'id_factura_compra',
            'precio',
            'cantidad',
            'descuento',
        ]
        read_only_fields = ['id_producto','id_factura_compra']
