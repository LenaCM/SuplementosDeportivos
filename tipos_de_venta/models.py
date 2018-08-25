from django.db import models

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