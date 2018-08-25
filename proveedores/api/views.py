from django.db.models import Q 
from rest_framework import generics, mixins

from proveedores.models import Proveedor

from .permissions import IsOwnerOrReadOnly
from .serializers import ProveedorSerializer

class ProveedorLC(mixins.CreateModelMixin, generics.ListAPIView):
    
    lookup_field='pk'
    serializer_class = ProveedorSerializer

    def get_queryset(self):
        qs =  Proveedor.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(nombre__icontains=query)|
                Q(descripcion__icontains=query)
            ).distinct()
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class ProveedorRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='pk'
    serializer_class = ProveedorSerializer
    #permission_classes = [IsOwnerOrReadOnly]
    
    def get_queryset(self):
        return Proveedor.objects.all()
