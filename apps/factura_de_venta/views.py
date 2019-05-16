from django.shortcuts import render
from rest_framework import viewsets

from apps.factura_de_venta.models import (
    facturaVenta,
    facturaVentaContieneProductos,
    TipoDeVenta,
    MedioDePago
)
from .serializers import (
    TipoDeVentaSerializer,
    MedioDePagoSerializer,
    facturaVentaSerializer,
    facturaVentaContieneProductosSerializer
)

class TipoDeVentaViewSet(viewsets.ModelViewSet):
    queryset = TipoDeVenta.objects.all()
    serializer_class = TipoDeVentaSerializer

class MedioDePagoViewSet(viewsets.ModelViewSet):
    queryset = MedioDePago.objects.all()
    serializer_class = MedioDePagoSerializer   

class facturaVentaViewSet(viewsets.ModelViewSet):
    queryset = facturaVenta.objects.all()
    serializer_class = facturaVentaSerializer   

class facturaVentaContieneProductosViewSet(viewsets.ModelViewSet):
    queryset = facturaVentaContieneProductos.objects.all()
    serializer_class = facturaVentaContieneProductosSerializer           
