from productos.models import Producto
from rest_framework import viewsets
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Producto.objects.all().order_by('nombre')
    serializer_class = ProductoSerializer

    