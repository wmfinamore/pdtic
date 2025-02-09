from django.contrib import admin
from .models import TipoAmbiente, TipoAvaliacao, Swot
from .forms import TipoAmbienteForm, TipoAvaliacaoForm, SwotForm
from simple_history.admin import SimpleHistoryAdmin


@admin.register(TipoAmbiente)
class TipoAmbienteAdmin(SimpleHistoryAdmin):
    form = TipoAmbienteForm
    model = TipoAmbiente
    list_display = ['id', 'nome']
    search_fields = ['nome']


@admin.register(TipoAvaliacao)
class TipoAvaliacaoAdmin(SimpleHistoryAdmin):
    form = TipoAvaliacaoForm
    model = TipoAvaliacao
    list_display = ['id','tipo_ambiente', 'nome']
    search_fields = ['nome']
    autocomplete_fields = ['tipo_ambiente']


@admin.register(Swot)
class SwotAdmin(SimpleHistoryAdmin):
    form = SwotForm
    model = Swot
    list_display = ['codigo', 'tipo_ambiente', 'tipo_avaliacao', 'descricao']
    search_fields = ['descricao']
    list_filter = ['tipo_ambiente', 'tipo_avaliacao']
