# Generated by Django 2.0.4 on 2018-06-10 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturaCompra', '0003_auto_20180606_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturacompra',
            name='idProveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.Proveedor', verbose_name='Nombre del proveedor'),
        ),
        migrations.AlterField(
            model_name='facturacompracontieneproductos',
            name='idProducto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='productos.Producto', verbose_name='Nombre del producto'),
        ),
    ]