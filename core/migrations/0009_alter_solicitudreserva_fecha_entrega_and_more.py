# Generated by Django 4.1.5 on 2023-01-23 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_articulos_solicitudreserva_delete_contacto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudreserva',
            name='fecha_entrega',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='solicitudreserva',
            name='fecha_salida',
            field=models.DateTimeField(null=True),
        ),
    ]
