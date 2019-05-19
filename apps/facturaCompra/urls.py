from django.urls import include, path
from . import views

app_name = "facturaCompra"

urlpatterns = [
    path('', views.index, name="index"),
    path('nuevo/', views.nuevaFacturaCompra.as_view(), name="nuevo"),
]