# Generated by Django 2.0.4 on 2018-04-17 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('idFactura', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('total', models.FloatField()),
            ],
        ),
    ]