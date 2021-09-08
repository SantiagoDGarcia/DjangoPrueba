# Generated by Django 3.1.7 on 2021-09-01 05:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_auto_20210831_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefono',
            name='entrega',
            field=models.CharField(blank=True, choices=[('Entregado', 'Entregado'), ('Enviado', 'Enviado')], default='Entregado', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='fecha_compra',
            field=models.DateField(default=datetime.date(2021, 9, 1)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='fecha',
            field=models.DateField(default=datetime.date(2021, 9, 1)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='hora',
            field=models.TimeField(default=datetime.time(0, 14, 55, 541797)),
        ),
    ]
