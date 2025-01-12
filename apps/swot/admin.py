from django.contrib import admin
from .models import TipoAmbiente, TipoAvaliacao
from .forms import TipoAmbienteForm, TipoAvaliacaoForm
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
