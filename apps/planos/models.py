from django.db import models
from apps.core.models import Auditoria


class PrincipioDiretriz(Auditoria):
    codigo = models.CharField(max_length=10, db_comment='Código do princípio ou diretriz levantada')
    principio_diretriz = models.CharField(max_length=250, db_comment='Descrição do princípio ou diretriz que precisa ser'
                                                                     ' observada no PDTIC')
    origem = models.CharField(max_length=100, db_comment='Nome do documento de origem do princípio ou diretriz')
    criterio_priorizacao = models.BooleanField(default=False, db_comment='Indica se o princípio ou diretriz é critério '
                                                                         'de priorização das necessidades')

    def __str__(self):
        resumo_diretriz = self.principio_diretriz[:50]
        return f"{self.codigo} - {resumo_diretriz}"

    class Meta:
        ordering = ['codigo', 'origem', ]
        verbose_name = 'Princípio ou Diretriz'
        verbose_name_plural = 'Princípios ou Diretrizes'
        db_table_comment = 'Lista de princípios ou diretrizes que devem ser observadas na produção do PDTIC'
        constraints = [
            models.UniqueConstraint(fields=['codigo'], name='unique_codigo_principio_diretriz'),
        ]



