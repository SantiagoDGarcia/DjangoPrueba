# Generated by Django 3.1.7 on 2021-09-03 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_auto_20210901_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(choices=[('Samsung', 'Samsung'), ('Apple', 'Apple')], default='Apple', max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Accesorios',
                'ordering': ['marca', 'nombre'],
            },
        ),
        migrations.AddField(
            model_name='telefono',
            name='llego_audifonos',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='telefono',
            name='llego_cargador',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='telefono',
            name='sefue_audifonos',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='telefono',
            name='sefue_cargador',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='entrega',
            field=models.CharField(blank=True, choices=[('Entregado', 'Entregado'), ('Envio servientrega', 'Envio servientrega'), ('Envio cooperativa', 'Envio cooperativa')], default='Entregado', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='fecha_compra',
            field=models.DateField(default=datetime.date(2021, 9, 3)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='fecha',
            field=models.DateField(default=datetime.date(2021, 9, 3)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='hora',
            field=models.TimeField(default=datetime.time(12, 15, 53, 841010)),
        ),
    ]
