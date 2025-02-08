from django.db import models
from apps.core.models import Auditoria
from apps.necessidades.models import NecessidadeTI
from apps.secretarias.models import Secretaria
from apps.equipes.models import Competencia
from apps.indicadores.models import Indicador


class Meta(Auditoria):
    codigo = models.CharField(max_length=10, db_comment='Código da meta', unique=True)
    nome = models.TextField(db_comment='Nome da meta', unique=True)
    necessidades = models.ManyToManyField(NecessidadeTI, related_name='metas_necessidade')
    indicadores = models.ManyToManyField(Indicador, related_name='metas_indicador')
    valor_meta = models.TextField(db_comment='Valor a ser alcançado pelo indicador da meta')
    prazo = models.DateField(db_comment='Prazo para a meta alcançar o valor estipulado para o indicador')

    def __str__(self):
        return f"{self.codigo} - {self.nome[:50]}"

    class Meta:
        verbose_name = 'Meta'
        verbose_name_plural = 'Metas'
        db_table_comment = 'Metas relacionado com as necessidades inventariadas'
        ordering = ['codigo']


class Acao(Auditoria):
    codigo = models.CharField(max_length=10, db_comment='Código da ação', unique=True)
    metas = models.ManyToManyField(Meta, related_name='acoes_metas')
    nome = models.TextField(db_comment='Nome da ação', unique=True)
    areas_responsaveis = models.ManyToManyField(Secretaria, related_name='acoes_areas')
    data_inicio_estimada = models.DateField(db_comment='Data de início estimada para a ação')
    data_conclusao_estimada = models.DateField(db_comment='Data de conslusão estimada para a ação')

    quantidade_pessoas = models.PositiveIntegerField(null=True, blank=True, db_comment='Quantidade de pessoas para '
                                                                                       'executar a ação')
    competencias = models.ManyToManyField(Competencia, related_name='acoes_competencias')

    valor_investimento = models.DecimalField(max_digits=14, decimal_places=2, default='0.00',
                                             db_comment='Valor de investimento necessário para executar a ação')
    valor_custeio = models.DecimalField(max_digits=14, decimal_places=2, default='0.00',
                                        db_comment='Valor de custeio necessário para manter a ação depois de implantada')

    def __str__(self):
        return f"{self.codigo} - {self.nome[:50]}"

    class Meta:
        verbose_name = 'Ação'
        verbose_name_plural = 'Ações'
        db_table_comment = 'Ações relacionadas a um ou mais metas'
        ordering = ['codigo']
