# Generated by Django 3.1.2 on 2020-11-21 05:32

import costos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0007_auto_20201121_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastoempresa',
            name='periodo',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Diario'), (7, 'Semanal'), (30, 'Mensual'), (60, 'Bimestral'), (90, 'Trimestral'), (120, 'Cuatrimestral'), (180, 'Semestral'), (360, 'Anual')], default=costos.models.Periodo['MES']),
        ),
        migrations.AlterField(
            model_name='gastopersonal',
            name='periodo',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Diario'), (7, 'Semanal'), (30, 'Mensual'), (60, 'Bimestral'), (90, 'Trimestral'), (120, 'Cuatrimestral'), (180, 'Semestral'), (360, 'Anual')], default=costos.models.Periodo['MES']),
        ),
    ]
