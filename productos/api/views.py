from productos.models import Producto
from rest_framework import generics
from .serializers import ProductoSerializer

class ProductoCreate(generics.CreateAPIView):
    
    lookup_field='pk'
    serializer_class = ProductoSerializer
    
    def get_queryset(self):
        return Producto.objects.all()

class ProductoRUD(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field='pk'
    serializer_class = ProductoSerializer
    
    def get_queryset(self):
        return Producto.objects.all().order_by('nombre')
    

    