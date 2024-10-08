# Generated by Django 3.1.4 on 2024-10-01 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0008_auto_20210528_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastoempresa',
            name='monto',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='gastopersonal',
            name='monto',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='instrumento',
            name='valor_USD',
            field=models.DecimalField(decimal_places=2, help_text='Valor de reposición en dólares. Cotización dólar oficial según Banco Nación.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='alquiler_instrumentos',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Pago de alquileres ocasionales para este trabajo.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='ayudante',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Pago de jornales a ayudante/s.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='ccu',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Pago de sellados por CCU.', max_digits=10, verbose_name='Certificado Catastral Urgente'),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='citaciones',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Pago de envío / estampillados por notificaciones.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='dibujante',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Pago a dibujante/s.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='escrituras',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Gasto por pedidos al RGP.', max_digits=10, verbose_name='monto por escrituras'),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='estudio_titulos',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Gastos extra por Estudio de Títulos.', max_digits=10, verbose_name='estudio de títulos'),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='georreferenciacion',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Gastos extra por Georreferenciación.', max_digits=10, verbose_name='georreferenciación'),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='gestor',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Pago a gestores, comisionistas, fletes.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='impresiones',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Pago por ploteos / impresiones de documentación.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='mojones',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Gasto en hierros, estacas, pintura, cintas peligro.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='otros_gastos',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Otros gastos sin categorizar.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='seguros_especiales',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Pago de seguros ocasionales para este trabajo.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='viaticos',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Pago de alojamiento / comidas.', max_digits=10, verbose_name='viáticos'),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='visados',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Gastos en reparticiones públicas.', max_digits=10, verbose_name='monto por visados'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='costo_anual_reparaciones',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Estimado de reparaciones por año.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='costo_cochera',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Costo mensual de cochera / garage.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='costo_lavado',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Gastos mensuales en lavado.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='costo_lubricante',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Costo del lubricante (calcula cada 6 meses).', max_digits=10),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='costo_neumatico',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Costo de 1 neumático (calcula cada 40.000 km).', max_digits=10),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='costo_patente',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Costo de cada cuota de la patente.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='costo_rto',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Costo de Revisión Técnica Obligatoria.', max_digits=10, verbose_name='RTO'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='costo_seguro',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Costo mensual del seguro.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='costo_service',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Costo de Service general (calcula cada 10.000 km).', max_digits=10),
        ),
    ]
