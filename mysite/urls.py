from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, include
#from . import views
#from django.contrib.auth.models import User
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    
    path('admin/', admin.site.urls),
    #APIS
    path('api-productos/', include('apps.productos.api.urls')),
    path('api-proveedores/', include('apps.proveedores.api.urls')),
    path('api-factura-venta/', include('apps.factura_de_venta.api.urls')),
    path('api-factura-compra/', include('apps.factura_de_compra.api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    #path de la autenticacion
    path('accounts/',include('django.contrib.auth.urls')),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
   
   
]
