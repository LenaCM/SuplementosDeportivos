from django.apps import AppConfig

class FacturaVentaConfig(AppConfig):
    name = 'factura_de_venta'
    verbose_name = 'Gestionar facturas de Venta'

class FacturaVentaContieneProductosConfig(AppConfig):
    name = 'Facturas de Venta contiene productos' 

class TipoDeVentaConfig(AppConfig):
    name = 'Tipo de venta'
    
class MedioDePagoConfig(AppConfig):
    name = 'Medio de pago' 
