from rest_framework import serializers

from productos.models import Producto
from factura_de_venta.models import (
    facturaVenta,
    facturaVentaContieneProductos,
    TipoDeVenta,
    MedioDePago
)
#----------------------------------------------------------------------------------
class TipoDeVentaSerializer(serializers.Serializer):
    class Meta:
        model = TipoDeVenta
        fields = ('tipo_de_venta')

#----------------------------------------------------------------------------------
class MedioDePagoSerializer(serializers.Serializer):
    class Meta:
        model = MedioDePago
        fields = ('medio_de_pago')

#----------------------------------------------------------------------------------
class facturaVentaSerializer(serializers.ModelSerializer):
    tipo_de_venta = models.ForeignKey(TipoDeVenta, on_delete=models.CASCADE, verbose_name="tipo de venta")
    medio_de_pago = models.ForeignKey(MedioDePago, on_delete=models.CASCADE, verbose_name="Medio de pago")
    class Meta:
        model = facturaVenta
        fields = [
            'id_factura_de_venta',
            'id_medio_de_pago',
            'id_tipo_de_venta',
            'fecha',
            'total',
        ]
        read_only_fields = ['id_factura_de_venta','id_medio_de_pago','id_tipo_de_venta']

#----------------------------------------------------------------------------------
class facturaVentaContieneProductosSerializer(serializers.ModelSerializer):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Producto")
    factura_de_venta = models.ForeignKey(facturaVenta, on_delete=models.CASCADE)
    class Meta:
        model = facturaVentaContieneProductos
        fields = [
            'pk',
            'precio',
            'cantidad',
            'descuento',
        ]
        read_only_fields = ['pk','id_producto','id_factura_de_venta']

#esta clase convierte a json y ademas valida  
# ejemplo de validacion min 21.33      