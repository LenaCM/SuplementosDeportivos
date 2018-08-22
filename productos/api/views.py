from productos.models import Producto
from rest_framework import generics, mixins
from .serializers import ProductoSerializer

class ProductoCreate(mixins.CreateModelMixin, generics.ListAPIView):
    
    lookup_field='pk'
    serializer_class = ProductoSerializer
    
    def get_queryset(self):
        return Producto.objects.all()
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class ProductoRUD(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field='pk'
    serializer_class = ProductoSerializer
    
    def get_queryset(self):
        return Producto.objects.all().order_by('nombre')
    

    