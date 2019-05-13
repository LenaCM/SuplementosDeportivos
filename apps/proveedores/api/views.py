from rest_framework import viewsets

from apps.proveedores.models import Proveedor
from .serializers import ProveedorSerializer

class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
