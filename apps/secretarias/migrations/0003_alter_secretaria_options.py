# Generated by Django 4.0.3 on 2022-10-19 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretarias', '0002_alter_historicalsecretaria_sigla_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='secretaria',
            options={'ordering': ['sigla']},
        ),
    ]
