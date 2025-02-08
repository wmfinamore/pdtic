from django.db import models
from apps.core.models import Auditoria
from sequences import get_next_value


class FonteDiretriz(models.Model):
    nome = models.CharField(max_length=100, db_comment='Nome da fonte de Diretrizes')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Fonte de Diretrizes'
        verbose_name_plural = 'Fontes de Diretrizes'
        db_table_comment = 'Lista de fontes de diretrizes(Planos Municipais, Leis, recomendação do TCESP, entre outros)'
        constraints = [
            models.UniqueConstraint(fields=['nome'], name='unique_nome_fonte_diretriz'),
        ]

class PrincipioDiretriz(Auditoria):
    codigo = models.CharField(max_length=10, editable=False, default='', db_comment='Código do princípio ou diretriz '
                                                                                    'levantada')
    principio_diretriz = models.TextField(db_comment='Descrição do princípio ou diretriz que precisa ser observada no '
                                                     'PDTIC')
    origem = models.ForeignKey(FonteDiretriz, on_delete=models.PROTECT, db_comment= 'Nome do documento de origem do '
                                                                                    'princípio ou diretriz')
    criterio_priorizacao = models.BooleanField(default=False, db_comment='Indica se o princípio ou diretriz é critério '
                                                                         'de priorização das necessidades')

    def save(self, *args, **kwargs):
        if self.codigo == '':
            codigo_diretriz = get_next_value("codigo_diretriz")
            self.codigo = f"D{codigo_diretriz}"
        super().save(*args, **kwargs)

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



