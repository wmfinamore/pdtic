# Generated by Django 5.1.4 on 2025-01-19 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipes', '0006_historicalinventariocompetencia_and_more'),
        ('metas', '0002_acao_historicalacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='acao',
            name='competencias',
            field=models.ManyToManyField(related_name='acoes_competencias', to='equipes.competencia'),
        ),
        migrations.AddField(
            model_name='acao',
            name='quantidade_pessoas',
            field=models.PositiveIntegerField(blank=True, db_comment='Quantidade de pessoas para executar a ação', null=True),
        ),
        migrations.AddField(
            model_name='acao',
            name='valor_custeio',
            field=models.DecimalField(db_comment='Valor de custeio necessário para manter a ação depois de implantada', decimal_places=2, default='0.00', max_digits=14),
        ),
        migrations.AddField(
            model_name='acao',
            name='valor_investimento',
            field=models.DecimalField(db_comment='Valor de investimento necessário para executar a ação', decimal_places=2, default='0.00', max_digits=14),
        ),
        migrations.AddField(
            model_name='historicalacao',
            name='quantidade_pessoas',
            field=models.PositiveIntegerField(blank=True, db_comment='Quantidade de pessoas para executar a ação', null=True),
        ),
        migrations.AddField(
            model_name='historicalacao',
            name='valor_custeio',
            field=models.DecimalField(db_comment='Valor de custeio necessário para manter a ação depois de implantada', decimal_places=2, default='0.00', max_digits=14),
        ),
        migrations.AddField(
            model_name='historicalacao',
            name='valor_investimento',
            field=models.DecimalField(db_comment='Valor de investimento necessário para executar a ação', decimal_places=2, default='0.00', max_digits=14),
        ),
    ]
