from django.urls import path, include
from .views import (
    TipoDeVentaLC,
    TipoDeVentaRUD,
)

urlpatterns = [
    path('', TipoDeVentaLC.as_view(), name='producto-create'),
    path('<int:pk>/', TipoDeVentaRUD.as_view(), name='producto-rud'),
]