# Generated by Django 5.1.4 on 2025-02-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('necessidades', '0003_historicalnecessidadeti_necessidadeti'),
        ('secretarias', '0004_alter_historicalsecretaria_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='necessidadeinformacao',
            name='areas_relacionadas',
            field=models.ManyToManyField(blank=True, to='secretarias.secretaria'),
        ),
        migrations.AlterField(
            model_name='necessidadeti',
            name='areas_relacionadas',
            field=models.ManyToManyField(to='secretarias.secretaria'),
        ),
    ]
