from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import TipoOrigem, NecessidadeInformacao, TipoNecessidade, NecessidadeTI
from .forms import TipoOrigemForm, NecessidadeInformacaoForm, TipoNecessidadeForm, NecessidadeTIForm


@admin.register(TipoOrigem)
class TipoOrigemAdmin(SimpleHistoryAdmin):
    form = TipoOrigemForm
    list_display = ['id', 'nome']
    search_fields = ['nome']


@admin.register(NecessidadeInformacao)
class NecessidadeInformacaoAdmin(SimpleHistoryAdmin):
    form = NecessidadeInformacaoForm
    list_display = ['codigo', 'descricao','estrategia_relacionada', 'origem']
    search_fields = ['codigo', 'descricao',]
    list_filter = ['origem', 'areas_relacionadas', 'estrategia_relacionada']
    autocomplete_fields = ['origem', 'estrategia_relacionada']
    filter_horizontal = ['areas_relacionadas' ]
    readonly_fields = ['codigo', ]


@admin.register(TipoNecessidade)
class TipoNecessidade(SimpleHistoryAdmin):
    form = TipoNecessidadeForm
    list_display = ['id', 'prefixo', 'nome', ]
    search_fields = ['nome', 'prefixo', ]


@admin.register(NecessidadeTI)
class NecessidadeTIAdmin(SimpleHistoryAdmin):
    form = NecessidadeTIForm
    list_display = ['codigo', 'descricao', 'tipo_necessidade', 'origem',]
    search_fields = ['codigo', 'descricao',]
    list_filter = ['origem', 'tipo_necessidade']
    autocomplete_fields = ['origem', 'tipo_necessidade', 'estrategia_relacionada',]
    filter_horizontal = ['areas_relacionadas']
    readonly_fields = ['codigo', ]
