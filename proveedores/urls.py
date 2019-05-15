from django.urls import include, path
from .views import ProveedorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('proveedores', ProveedorViewSet)

urlpatterns = [
    path('', include(router.urls))
]

'''
url(r'^$', views.index, name="index"),
    url(r'^nuevo/$', views.nuevoProveedor, name='nuevo'),
    url(r'^editar/(?P<pk>[0-9]+)/edit/$', views.editarProveedor, name='editar_proveedor'),
    url(r'^eliminar/(?P<pk>[0-9]+)/$', views.eliminarProveedor, name='eliminar_proveedor'),
    url(r'^busqueda/$', views.buscador, name="buscar_proveedor"),
'''