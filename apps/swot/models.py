from django.db import models
from apps.core.models import Auditoria


class TipoAmbiente(Auditoria):
    nome = models.CharField(max_length=100, unique=True, db_comment='No do tipo de ambiente')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tipo de Ambiente'
        verbose_name_plural = 'Tipos de Ambiente'
        db_table_comment = 'Tipos de ambiente na análise SWOT'
        ordering = ['nome']


class TipoAvaliacao(Auditoria):
    tipo_ambiente = models.ForeignKey(TipoAmbiente, on_delete=models.PROTECT, db_comment='Tipo de ambiente relacionado')
    nome = models.CharField(max_length=100, unique=True, db_comment='Nome do tipo de avaliação')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tipo de Avaliação'
        verbose_name_plural = 'Tipos de Avaliação'
        db_table_comment = 'Tipo de Avaliação da análise SWOT'
        ordering = ['nome']
