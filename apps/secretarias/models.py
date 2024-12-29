from django.db import models
from simple_history.models import HistoricalRecords


class Secretaria(models.Model):
    sigla = models.CharField(max_length=10, null=True, blank=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.sigla+' - ' + self.nome.title()

    class Meta:
        ordering = ['sigla']

    @property
    def qtd_projetos(self):
        qtd = int(self.secretaria_projetos.all().count())
        return qtd
