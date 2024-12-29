# Generated by Django 4.0.1 on 2022-01-17 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretarias', '0002_alter_historicalsecretaria_sigla_and_more'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='secretarias',
            field=models.ManyToManyField(blank=True, related_name='usuarios_secretarias', to='secretarias.Secretaria'),
        ),
    ]