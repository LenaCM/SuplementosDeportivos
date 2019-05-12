# Generated by Django 2.0.4 on 2018-08-20 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=300)),
                ('stock', models.SmallIntegerField()),
                ('stock_minimo', models.SmallIntegerField()),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_minorista', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_mayorista', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
