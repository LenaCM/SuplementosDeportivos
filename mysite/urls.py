from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.urls import path, include
from django.contrib.auth.models import User
from productos.urls import productos_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
#from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from .views import UserViewSet, CustomAuthToken
#from pages.urls import pages_patterns

router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('proveedores/', include('proveedores.urls')),
    path('auth/', CustomAuthToken.as_view()),
    path('user/', include(router.urls)),
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
