from django.db.models import Q 
from rest_framework import generics, mixins

from productos.models import Producto
from factura_de_venta.models import (
    facturaVenta,
    facturaVentaContieneProductos,
    TipoDeVenta,
    MedioDePago
)
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    TipoDeVentaSerializer,
    MedioDePagoSerializer,
    facturaVentaSerializer,
    facturaVentaContieneProductosSerializer
)

class TipoDeVentaLC(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field='pk'
    serializer_class = TipoDeVentaSerializer

    def get_queryset(self):
        qs =  TipoDeVenta.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(nombre__icontains=query)|
                Q(descripcion__icontains=query)
            ).distinct()
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class TipoDeVentaRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='pk'
    serializer_class = TipoDeVentaSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_queryset(self):
        return TipoDeVenta.objects.all()
    

    