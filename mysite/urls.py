#from django.conf.urls import include, url , 
from django.contrib import admin
from . import views
from django.urls import path, include
from productos.urls import productos_patterns
#from pages.urls import pages_patterns

urlpatterns = [
    
    #path('', include('core.urls')),
    #path('productos/', include(productos_patterns)),
    path('admin/', admin.site.urls),
    #path de REST framework
    path('api-auth/', include('rest_framework.urls')),
    path('api-productos/', include('productos.api.urls')),
    path('api-proveedores/',include('proveedores.api.urls')),
    #path de la autenticacion
    #path('accounts/',include('django.contrib.auth.urls')),
   
   
]
