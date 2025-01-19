from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Meta, Acao
from .forms import MetasForm, AcaoForm


@admin.register(Meta)
class MetaAdmin(SimpleHistoryAdmin):
    form = MetasForm
    list_display = ['codigo', 'nome', 'indicador', 'valor_meta', 'prazo', ]
    search_fields = ['codigo', 'nome', 'indicador', 'valor_meta', ]
    date_hierarchy = 'prazo'
    filter_horizontal = ['necessidades', ]


@admin.register(Acao)
class AcaoAdmin(SimpleHistoryAdmin):
    form = AcaoForm
    list_display = ['codigo', 'nome', 'data_inicio_estimada', 'data_conclusao_estimada']
    search_fields = ['codigo', 'nome',]
    date_hierarchy = 'data_conclusao_estimada'
    filter_horizontal = ['metas', 'areas_responsaveis', ]

