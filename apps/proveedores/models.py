from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
#pip install django-phonenumber-field 
#https://github.com/stefanfoulis/django-phonenumber-field ver como configurar (ej +41524204242)

class Proveedor(models.Model):
    
    nombre = models.CharField(max_length=50)
    telefono = PhoneNumberField()
    mail = models.EmailField(max_length=254)
    comentario = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.nombre
