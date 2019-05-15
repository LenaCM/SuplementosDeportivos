from django.urls import path, include
from .views import ProveedorLC, ProveedorRUD

urlpatterns = [
    path('', ProveedorLC.as_view(), name='lista-proveedor'),
    path('<int:pk>/', ProveedorRUD.as_view(), name='crud-proveedor'),
]