from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, CustomAuthToken

router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    #apps
    path('proveedores/', include('apps.proveedores.urls')),
    path('productos/', include('apps.productos.urls')),
    path('facturasVenta/', include('apps.factura_de_venta.urls')),
    path('facturasCompra/', include('apps.facturaCompra.urls')),
    path('user/', include(router.urls)),
    #authentication
    path('auth/', CustomAuthToken.as_view()),
    #path('', include('core.urls')),
    #path('productos/', include(productos_patterns)),
    #path de REST framework
    #url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    #path('api-productos/', include('productos.api.urls')),
    #path('api-proveedores/',include('proveedores.urls')),
    #path de la autenticacion
    #path('accounts/',include('django.contrib.auth.urls')),
    #path(r'api-token-auth/', obtain_jwt_token),
    #path(r'api-token-refresh/', refresh_jwt_token),
   
   
]
