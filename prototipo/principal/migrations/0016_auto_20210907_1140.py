# Generated by Django 3.1.7 on 2021-09-07 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0015_auto_20210907_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesorio',
            name='vendido',
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='hora',
            field=models.TimeField(default=datetime.time(11, 40, 53, 465466)),
        ),
    ]
