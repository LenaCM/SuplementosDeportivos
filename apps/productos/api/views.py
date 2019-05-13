#from django.db.models import Q 
from rest_framework import viewsets

from apps.productos.models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
    

#class ProductoLC(mixins.CreateModelMixin, generics.ListAPIView):
    
#    lookup_field='pk'
#    serializer_class = ProductoSerializer
    
#    def get_queryset(self):
#        qs =  Producto.objects.all()
#        query = self.request.GET.get("q")
#        if query is not None:
#            qs = qs.filter(
#                Q(nombre__icontains=query)|
#                Q(descripcion__icontains=query)
#            ).distinct()
#        return qs

#    def post(self,request,*args,**kwargs):
#        return self.create(request,*args,**kwargs)

#class ProductoRUD(generics.RetrieveUpdateDestroyAPIView):
    
#    lookup_field='pk'
#    serializer_class = ProductoSerializer
    
#    def get_queryset(self):
#        return Producto.objects.all().order_by('nombre')
