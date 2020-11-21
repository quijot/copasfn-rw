# Generated by Django 3.1.2 on 2020-11-21 04:52

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastoempresa',
            name='periodo',
            field=models.DecimalField(choices=[(1, 'Diario'), (Decimal('7.01923079999999988132231010240502655506134033203125'), 'Semanal'), (Decimal('30.416666666666667850904559600166976451873779296875'), 'Mensual'), (Decimal('60.83333333333333570180911920033395290374755859375'), 'Bimestral'), (Decimal('91.25'), 'Trimestral'), (Decimal('121.6666666666666714036182384006679058074951171875'), 'Cuatrimestral'), (Decimal('182.5'), 'Semestral'), (365, 'Anual')], decimal_places=7, default=Decimal('30.416666666666667850904559600166976451873779296875'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='gastopersonal',
            name='periodo',
            field=models.DecimalField(choices=[(1, 'Diario'), (Decimal('7.01923079999999988132231010240502655506134033203125'), 'Semanal'), (Decimal('30.416666666666667850904559600166976451873779296875'), 'Mensual'), (Decimal('60.83333333333333570180911920033395290374755859375'), 'Bimestral'), (Decimal('91.25'), 'Trimestral'), (Decimal('121.6666666666666714036182384006679058074951171875'), 'Cuatrimestral'), (Decimal('182.5'), 'Semestral'), (365, 'Anual')], decimal_places=7, default=Decimal('30.416666666666667850904559600166976451873779296875'), max_digits=10),
        ),
    ]
