from django.urls import path, include
from rest_framework import routers

from .views import ProveedoresViewSet

router = routers.DefaultRouter()
router.register('proveedores', ProveedoresViewSet)

urlpatterns = [
    
    path('', include(router.urls)),
   
]