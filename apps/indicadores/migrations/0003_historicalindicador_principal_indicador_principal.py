# Generated by Django 5.1.6 on 2025-02-09 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0002_historicalindicador_codigo_indicador_codigo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalindicador',
            name='principal',
            field=models.BooleanField(db_comment='Indicador principal', default=False),
        ),
        migrations.AddField(
            model_name='indicador',
            name='principal',
            field=models.BooleanField(db_comment='Indicador principal', default=False),
        ),
    ]
