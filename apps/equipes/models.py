from django.db import models
from apps.core.models import Auditoria


class TipoCompetencia(Auditoria):
    tipo_competencia = models.CharField(max_length=50, db_comment='Tipo de competência')
    descricao = models.TextField(null=True, blank=True, db_comment='Descrição do tipo de competência')

    def __str__(self):
        return self.tipo_competencia

    class Meta:
        ordering = ['tipo_competencia']
        verbose_name = 'Tipo de Competência'
        verbose_name_plural = 'Tipos de Competência'
        db_table_comment = 'Registro dos tipos de competência'


class Competencia(Auditoria):
    tipo_competencia = models.ForeignKey(TipoCompetencia, on_delete=models.PROTECT, related_name='competencias',
                                         db_comment='Identificador do tipo de competência')
    competencia = models.CharField(max_length=100, unique=True, db_comment='Nome da competência')
    descricao = models.TextField(null=True, blank=True, db_comment='Descrição da competência')

    def __str__(self):
        return self.competencia

    class Meta:
        ordering = ['competencia']
        verbose_name = 'Competência'
        verbose_name_plural = 'Competências'
        db_table_comment = 'Registro de competências'


class Desenvolvedor(Auditoria):
    nome = models.CharField(max_length=100, db_comment='Nome completo do desenvolvedor')
    matricula = models.CharField(max_length=10, null=True, blank=True, unique=True,
                                 db_comment='Matricula do desenvolvedor')
    email = models.EmailField(null=True, blank=True, db_comment='E-mail do desenvolvedor')
    ativo = models.BooleanField(default=True, db_comment='Indicador para desenvolvedor ativo')

    def __str__(self):
        return f"{self.matricula}-{self.nome}"

    class Meta:
        ordering = ['nome', 'matricula']
        verbose_name = 'Desenvolvedor'
        verbose_name_plural = 'Desenvolvedores'
        db_table_comment = 'Registro dos desenvolvedores'


class NivelCompetencia(Auditoria):
    nivel = models.CharField(max_length=50, unique=True, db_comment='Nível da Competência')
    descricao = models.TextField(db_comment='Descrição do nível')

    def __str__(self):
        return self.nivel

    class Meta:
        ordering = ['id',]
        verbose_name = 'Nível da Competência'
        verbose_name_plural = 'Niveis da Competência'
        db_table_comment = 'Registro de nível de competência'


class InventarioCompetencia(Auditoria):
    desenvolvedor = models.ForeignKey(Desenvolvedor, on_delete=models.PROTECT,
                                      db_comment='Identificador do desenvolvedor',)
    competencia = models.ForeignKey(Competencia, on_delete=models.PROTECT, db_comment='Identificador da competencia')
    aquisicao_competencia = models.TextField(null=True, blank=True, db_comment='relato da aquisição da competência')
    nivel = models.ForeignKey(NivelCompetencia, on_delete=models.PROTECT,
                              db_comment='Identificador do nível da competência')

    def __str__(self):
        return f"{self.desenvolvedor}-{self.competencia}"

    class Meta:
        ordering = ['desenvolvedor', 'competencia']
        verbose_name = 'Inventário de Competências'
        verbose_name_plural = 'Inventários de Competências'
        db_table_comment = 'Registro do inventário de competências'
        constraints = [
            models.UniqueConstraint(fields=['desenvolvedor', 'competencia'], name='unique_desenvolvedor_competencia'),
        ]
