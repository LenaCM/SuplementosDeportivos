from django.contrib import admin
from .models import facturaCompra , facturaCompraContieneProductos

class facturaCompraAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor','total')
    date_hierarchy = 'fecha'
    search_fields = ('id_proveedor',)
    list_filter = ('id_proveedor',)

class facturaCompraContieneProductosAdmin(admin.ModelAdmin):
    list_display = ('id_producto','precio','cantidad','descuento')

   
admin.site.register(facturaCompra,facturaCompraAdmin)
admin.site.register(facturaCompraContieneProductos,facturaCompraContieneProductosAdmin)

