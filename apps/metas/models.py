from django.db import models
from apps.core.models import Auditoria
from apps.necessidades.models import NecessidadeTI


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
