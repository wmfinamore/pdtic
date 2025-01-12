from django.contrib import admin
from .models import TipoAmbiente
from .forms import TipoAmbienteForm
from simple_history.admin import SimpleHistoryAdmin


@admin.register(TipoAmbiente)
class TipoAmbienteAdmin(SimpleHistoryAdmin):
    form = TipoAmbienteForm
    model = TipoAmbiente
    list_display = ['id', 'nome']
    search_fields = ['nome']
