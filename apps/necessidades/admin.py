from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import TipoOrigem, NecessidadeInformacao
from .forms import TipoOrigemForm, NecessidadeInformacaoForm


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
