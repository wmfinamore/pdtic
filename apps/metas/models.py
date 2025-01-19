from django.db import models
from apps.core.models import Auditoria
from apps.necessidades.models import NecessidadeTI
from apps.secretarias.models import Secretaria


class Meta(Auditoria):
    codigo = models.CharField(max_length=10, db_comment='Código da meta', unique=True)
    nome = models.TextField(db_comment='Nome da meta', unique=True)
    necessidades = models.ManyToManyField(NecessidadeTI, db_comment='Necessidades relacionadas com a meta',
                                         related_name='metas_necessidade')
    indicador = models.TextField(db_comment='Indicador de meta relacionado com a meta')
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
    metas = models.ManyToManyField(Meta, db_comment='Metas relacionadas com uma ação', related_name='acoes_metas')
    nome = models.TextField(db_comment='Nome da ação', unique=True)
    areas_responsaveis = models.ManyToManyField(Secretaria, db_comment='Áreas responsáveis pela ação',
                                                related_name='acoes_areas')
    data_inicio_estimada = models.DateField(db_comment='Data de início estimada para a ação')
    data_conclusao_estimada = models.DateField(db_comment='Data de conslusão estimada para a ação')

    def __str__(self):
        return f"{self.codigo} - {self.descricao[:50]}"

    class Meta:
        verbose_name = 'Ação'
        verbose_name_plural = 'Ações'
        db_table_comment = 'Ações relacionadas a um ou mais metas'
        ordering = ['codigo']
