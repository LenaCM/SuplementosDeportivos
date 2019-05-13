from django.urls import path, include
from rest_framework import routers

from apps.factura_de_compra.models import facturaCompra, facturaCompraContieneProductos
from .views import facturaCompraViewSet, facturaCompraContieneProductosViewSet

router = routers.DefaultRouter()
router.register('fac-compra', facturaCompraViewSet)
router.register('fac-compra-prod', facturaCompraContieneProductosViewSet)

urlpatterns = [
    
    path('', include(router.urls)),
   
]