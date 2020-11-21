# Generated by Django 3.1.2 on 2020-11-21 05:01

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0004_auto_20201121_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastoempresa',
            name='periodo',
            field=models.DecimalField(choices=[(1, 'Diario'), (Decimal('7.019230768999999980906068230979144573211669921875'), 'Semanal'), (Decimal('30.416666670000001460039129597134888172149658203125'), 'Mensual'), (Decimal('60.8333333300000020926745492033660411834716796875'), 'Bimestral'), (Decimal('91.25'), 'Trimestral'), (Decimal('121.6666666999999932841092231683433055877685546875'), 'Cuatrimestral'), (Decimal('182.5'), 'Semestral'), (365, 'Anual')], decimal_places=49, default=Decimal('30.416666666666667850904559600166976451873779296875'), max_digits=52),
        ),
        migrations.AlterField(
            model_name='gastopersonal',
            name='periodo',
            field=models.DecimalField(choices=[(1, 'Diario'), (Decimal('7.019230768999999980906068230979144573211669921875'), 'Semanal'), (Decimal('30.416666670000001460039129597134888172149658203125'), 'Mensual'), (Decimal('60.8333333300000020926745492033660411834716796875'), 'Bimestral'), (Decimal('91.25'), 'Trimestral'), (Decimal('121.6666666999999932841092231683433055877685546875'), 'Cuatrimestral'), (Decimal('182.5'), 'Semestral'), (365, 'Anual')], decimal_places=49, default=Decimal('30.416666666666667850904559600166976451873779296875'), max_digits=52),
        ),
    ]
