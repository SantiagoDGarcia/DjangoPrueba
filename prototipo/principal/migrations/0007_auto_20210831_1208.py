# Generated by Django 3.1.7 on 2021-08-31 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_auto_20210831_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='hora',
            field=models.TimeField(default=datetime.time(12, 8, 2, 755430)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='motivo',
            field=models.CharField(blank=True, default='Ninguno', max_length=100, null=True),
        ),
    ]
