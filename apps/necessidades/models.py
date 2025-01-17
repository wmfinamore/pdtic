from django.db import models
from apps.core.models import Auditoria
from apps.planos.models import PrincipioDiretriz
from apps.secretarias.models import Secretaria


class TipoOrigem(Auditoria):
    nome = models.CharField( max_length=100, unique=True, db_comment='Nome da origem da necessidade')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Origem'
        verbose_name_plural = 'Origens'
        db_table_comment = 'Tipos de origem de uma necessidade'
        ordering = ['nome']


class NecessidadeInformacao(Auditoria):
    codigo = models.CharField(max_length=10, unique=True, db_comment='Código da necessidade de informação')
    descricao = models.TextField(db_comment='Descrição da necessidade de informação')
    estrategia_relacionada = models.ForeignKey(PrincipioDiretriz, on_delete=models.PROTECT, null=True, blank=True,
                                               db_comment='Princípio ou diretriz relacionada com a necessidade de '
                                                          'informação')
    origem = models.ForeignKey(TipoOrigem, on_delete=models.PROTECT, db_comment='Tipo de origem da necessidade')
    areas_relacionadas = models.ManyToManyField(Secretaria, blank=True, db_comment='Secretarias relacionadas com a '
                                                                                   'necessidade de informação')

    def __str__(self):
        return f"{self.codigo} - {self.descricao[:50]}"

    class Meta:
        verbose_name = 'Necessidade de Informação'
        verbose_name_plural = 'Necessidades de Informação'
        db_table_comment = 'Necessidades de informação para o PDTIC'
        ordering = ['codigo']

class TipoNecessidade(Auditoria):
    nome = models.CharField(max_length=50, unique=True, db_comment='Nome do tipo de necessidade')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tipo de Necessidade'
        verbose_name_plural = 'Tipos de Necessidade'
        db_table_comment = 'Tipos de necessidade para o PDTIC'
        ordering = ['nome', ]
