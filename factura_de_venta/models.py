from django.db import models
from django.utils import timezone
#importo modelos
from mediosDePago.models import MedioDePago
from tiposDeVenta.models import TipoDeVenta
from productos.models import Producto

# Create your models here.
class TipoDeVenta(models.Model):
    
    OPCION1 = 'PO1'
    OPCION2 = 'P02'

    OPCIONES_TIPO_DE_VENTA = (
        (OPCION1, 'Opcion 1'),
        (OPCION2, 'Opcion 2'),
    )

    tipo_de_venta = models.CharField(max_length=50, choices=OPCIONES_TIPO_DE_VENTA, default=OPCION1)
    
    class Meta:
        verbose_name = "Tipo de venta"
        verbose_name_plural = "Tipos de venta"

    def __str__(self):
        return self.tipo_de_venta
        
class facturaVenta(models.Model):
    idFacturaVenta = models.BigAutoField(primary_key=True)
    idMedioDePago = models.ForeignKey(MedioDePago, on_delete=models.CASCADE, verbose_name="Medio de pago")
    idTipoDeVenta = models.ForeignKey(TipoDeVenta, on_delete=models.CASCADE, verbose_name="tipo de venta")
    fecha = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
    class Meta:
        verbose_name = "Factura de venta"
        verbose_name_plural = "Facturas de venta"

class facturaVentaContieneProductos(models.Model):
    idProducto = models.ForeignKey(Producto, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Producto")
    idfacturaVenta = models.ForeignKey(facturaVenta, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    cantidad = models.IntegerField()
    descuento = models.DecimalField(max_digits=10,decimal_places=2)  

    class Meta:
        verbose_name = "Factura de venta contiene productos"
        verbose_name_plural = "Facturas de venta contiene productos"