from django.db import models
from django.utils import timezone
from apps.proveedores.models import Proveedor
from apps.productos.models import Producto

class facturaCompra(models.Model):
    id_factura_compra = models.BigAutoField(primary_key=True)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name="Nombre del proveedor")
    fecha = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
    class Meta:
        verbose_name = "Factura de compra"
        verbose_name_plural = "Facturas de compra"
    
class facturaCompraContieneProductos(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Nombre del producto")
    id_factura_compra = models.ForeignKey(facturaCompra, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    cantidad = models.IntegerField()
    descuento = models.DecimalField(max_digits=10,decimal_places=2)  

    class Meta:
        verbose_name = "Factura de compra contiene productos"
        verbose_name_plural = "Facturas de compra contiene productos"
