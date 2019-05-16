from django.contrib import admin
from django.contrib import admin
from .models import (
    facturaVenta, 
    facturaVentaContieneProductos,
    MedioDePago,
    TipoDeVenta
)

class facturaVentaAdmin(admin.ModelAdmin):
    list_display = ('id_medio_de_pago', 'id_tipo_de_venta', 'total')
    date_hierarchy = 'fecha'
    list_filter = ('id_tipo_de_venta',)

class facturaVentaContieneProductosAdmin(admin.ModelAdmin):
    list_display = ('id_producto','precio','cantidad','descuento')

class TipoDeVentaAdmin(admin.ModelAdmin):
    list_display = ('tipo_de_venta',)
    
class MedioDePagoAdmin(admin.ModelAdmin):
    list_display = ('medio_de_pago',) 

admin.site.register(facturaVenta,facturaVentaAdmin)
admin.site.register(facturaVentaContieneProductos,facturaVentaContieneProductosAdmin)
admin.site.register(TipoDeVenta,TipoDeVentaAdmin)
admin.site.register(MedioDePago,MedioDePagoAdmin)
