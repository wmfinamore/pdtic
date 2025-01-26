from django.db import models
from apps.core.models import Auditoria
from apps.secretarias.models import Secretaria


class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=100, unique=True, db_comment='Nome da unidade de medido')
    valor_fracionado = models.BooleanField(default=False, db_comment='Unidade de medida permite valor fracionado?')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Unidade de Medida'
        verbose_name_plural = 'Unidades de Medida'
        ordering = ['nome', ]
        db_table_comment = 'Unidades de Medida'


class Periodicidade(models.Model):
    nome = models.CharField(max_length=100, unique=True, db_comment='Nome da periodicidade')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Periodicidade'
        verbose_name_plural = 'Periodicidades'
        ordering = ['nome', ]
        db_table_comment = 'Periodicidade para medição dos indicadores'


SENTIDO =   [
    ['MELHOR_CIMA', 'Melhor para cima'],
    ['MELHOR_BAIXO', 'Melhor para baixo']
]

class Indicador(Auditoria):
    secretaria = models.ForeignKey(Secretaria, on_delete=models.PROTECT,
                                   db_comment='Secretaria responsável pelo indicador')
    nome = models.CharField(max_length=120, db_comment='Nome do indicador')
    formula = models.TextField(db_comment='Fórmula do indicador')
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.PROTECT,
                                       db_comment='Unidade de medida do indicador')
    responsavel = models.CharField(max_length=120, null=True, blank=True,
                                   db_comment='Pessoal responsável pelo indicador')
    fonte_dados = models.CharField(max_length=120, null=True, blank=True,
                                   db_comment='Fonte de dados para aferição do indicador')
    resultado_atual = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True,
                                          db_comment='Resultado atual do indicador')
    valor_meta = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True,
                                          db_comment='Valor da meta para o indicador')
    periodicidade = models.ForeignKey(Periodicidade, on_delete=models.PROTECT,
                                      db_comment='Periodicidade de medição do indicador')
    sentido = models.CharField(max_length=120, choices=SENTIDO, db_comment='Sentido do indicador' )

    def __str__(self):
        return f"{self.id}-{self.nome}"

    class Meta:
        verbose_name = 'Indicador'
        verbose_name_plural = 'Indicadores'
        ordering = ['nome', ]
        db_table_comment = 'Indicadores chave de desempenho'
        default_related_name = 'indicadores'
