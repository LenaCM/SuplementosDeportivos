from django.urls import path, include
from rest_framework import routers

from .views import (
    TipoDeVentaViewSet,
    MedioDePagoViewSet,
    facturaVentaViewSet,
    facturaVentaContieneProductosViewSet
)

router = routers.DefaultRouter()
router.register('tipo-de-venta', TipoDeVentaViewSet)
router.register('medio-de-pago', MedioDePagoViewSet)
router.register('fac-venta', facturaVentaViewSet)
router.register('fac-venta-prod', facturaVentaContieneProductosViewSet)


urlpatterns = [
    
    path('', include(router.urls)),
   
]