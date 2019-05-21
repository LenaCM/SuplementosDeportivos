from .models import facturaCompra , facturaCompraContieneProductos
from apps.proveedores.models import Proveedor
from apps.productos.models import Producto
from rest_framework import viewsets
from .serializers import facturaCompraSerializer, facturaCompraContieneProductosSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import json

class facturaCompraViewSet(viewsets.ModelViewSet):
    serializer_class = facturaCompraSerializer
    queryset = facturaCompra.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        queryset = facturaCompra.objects.all()
        serializer = facturaCompraSerializer(queryset, many=True)
        return Response({
            'mensaje': 'Estos son las facturas de compra',
            'facturas': serializer.data
        })
    
    def create(self, request):
        proveedorId = request.data['idProveedor']
        proveedor = Proveedor.objects.get(id=proveedorId)
        total = request.data['total']
        fecha = request.data['fecha']
        try:
            factura = facturaCompra.objects.create(total=total, idProveedor=proveedor)

            facturaS = facturaCompraSerializer(factura, many=False)

            productosJSON = json.loads(request.data['productos'])
            tam = len(productosJSON)
            productos = []
            for i in range(tam):
                producto = Producto.objects.get(id=productosJSON[i]['id'])
                productos.append(facturaCompraContieneProductos(idProducto=producto, precio=productosJSON[i]['precio'], cantidad=productosJSON[i]['cantidad'], descuento=productosJSON[i]['descuento'], idFacturaCompra=factura))
            
            try:
                productosFactura = facturaCompraContieneProductos.objects.bulk_create(productos)
                productosFacturaS = facturaCompraContieneProductosSerializer(productosFactura, many=True)

                return Response({
                    'success': True,
                    'mensaje': 'Se guardó la factura correctamente',
                    'factura': facturaS.data,
                    'productos': productosFacturaS.data
                })
            except:
                return Response({
                'success': False,
                'mensaje': 'No se pudo registrar la factura'
            })

        except:
            return Response({
                'success': False,
                'mensaje': 'No se pudo registrar la factura'
            })



