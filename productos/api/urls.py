from django.urls import path, include
from .views import ProductoRUD, ProductoCreate

urlpatterns = [
    path('', ProductoCreate.as_view(), name='producto-create'),
    path('<int:pk>/', ProductoRUD.as_view(), name='producto-rud'),
]