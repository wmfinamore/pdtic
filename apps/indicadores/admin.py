from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import UnidadeMedida, Periodicidade, Indicador
from .forms import UnidadeMedidaForm, PeriodicidadeForm, IndicadorForm


@admin.register(UnidadeMedida)
class UnidadeMedidaAdmin(SimpleHistoryAdmin):
    form = UnidadeMedidaForm
    list_display = ['nome', 'valor_fracionado']
    search_fields = ['nome', ]


@admin.register(Periodicidade)
class PeriodicidadeAdmin(SimpleHistoryAdmin):
    form = PeriodicidadeForm
    list_display = ['nome', ]
    search_fields = ['nome', ]


@admin.register(Indicador)
class IndicadorAdmin(SimpleHistoryAdmin):
    form = IndicadorForm
    list_display = ['nome', 'secretaria', 'periodicidade', 'sentido', 'fonte_dados', 'resultado_atual', 'valor_meta']
    autocomplete_fields = ['periodicidade', 'unidade_medida', ]
    search_fields = ['nome', 'formula', ]
    list_filter = ['periodicidade', 'unidade_medida', 'secretaria', ]
