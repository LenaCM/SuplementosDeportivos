from django.urls import path, include
from .views import ProductoLC, ProductoRUD

urlpatterns = [
   path('', ProductoLC.as_view(), name='producto-create'),
   path('<int:pk>/', ProductoRUD.as_view(), name='producto-rud'),
   
]
