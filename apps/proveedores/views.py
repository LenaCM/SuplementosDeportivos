from django.db.models import Q 
from .models import Proveedor
from rest_framework import viewsets, generics, mixins
from .serializers import ProveedoresSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly

class ProveedorViewSet(viewsets.ModelViewSet):
    serializer_class = ProveedoresSerializer
    queryset = Proveedor.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,) #para restringir la manipulacion de estos datso en caso que por defecto se permita acceder desde settings


class ProveedorLC(mixins.CreateModelMixin, generics.ListAPIView):
    
    lookup_field='pk'
    serializer_class = ProveedoresSerializer

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
    serializer_class = ProveedoresSerializer
    #permission_classes = [IsOwnerOrReadOnly]
    
    def get_queryset(self):
        return Proveedor.objects.all()