from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets

from apps.factura_de_compra.models import facturaCompra, facturaCompraContieneProductos
from .serializers import FacturaCompraSerializer, facturaCompraContieneProductosSerializer

class facturaCompraViewSet(viewsets.ModelViewSet):
    queryset = facturaCompra.objects.all()
    serializer_class = FacturaCompraSerializer

class facturaCompraContieneProductosViewSet(viewsets.ModelViewSet):
    queryset = facturaCompraContieneProductos.objects.all()
    serializer_class = facturaCompraContieneProductosSerializer    
