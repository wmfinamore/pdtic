from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Meta
from .forms import MetasForm


@admin.register(Meta)
class MetaAdmin(SimpleHistoryAdmin):
    form = MetasForm
    model = Meta
    list_display = ['codigo', 'nome', 'indicador', 'valor_meta', 'prazo', ]
    search_fields = ['codigo', 'nome', 'indicador', 'valor_meta', ]
    date_hierarchy = 'prazo'
    filter_horizontal = ['necessidades', ]
