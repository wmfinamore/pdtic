from django.db import models
from apps.core.models import Auditoria
from smart_selects.db_fields import ChainedForeignKey
from sequences import get_next_value


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


class Swot(Auditoria):
    codigo = models.CharField(max_length=5, editable=False, default='', db_comment='Codigo da avaliação SWOT')
    tipo_ambiente = models.ForeignKey(TipoAmbiente, on_delete=models.PROTECT, db_comment='Tipo de ambiente')
    tipo_avaliacao = ChainedForeignKey(
        TipoAvaliacao,
        chained_field='tipo_ambiente',
        chained_model_field='tipo_ambiente',
        show_all=False,
        auto_choose=True,
        sort=True)
    descricao = models.TextField(db_comment='Descrição do ponto analisado')

    def save(self, *args, **kwargs):
        if self.codigo == '':
            codigo_swot = get_next_value('codigo_swot')
            self.codigo = f"SW{codigo_swot}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Swot'
        verbose_name_plural = 'Swots'
        ordering = ['descricao']
        constraints = [
            models.UniqueConstraint(fields=['codigo'], name='unique_codigo_swot'),
        ]
