from django.conf.urls import url, include
from productos.api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'productos', views.ProductoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]