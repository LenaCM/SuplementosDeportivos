from django.urls import include, path
from .views import ProveedorViewSet, ProveedorLC, ProveedorRUD
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', ProveedorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('lista', ProveedorLC.as_view(), name='lista-proveedor'),
    path('<int:pk>/', ProveedorRUD.as_view(), name='crud-proveedor'),
]