from django.urls import include, path
from .views import facturaCompraViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', facturaCompraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]