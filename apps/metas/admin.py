from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Meta, Acao
from .forms import MetasForm, AcaoForm


@admin.register(Meta)
class MetaAdmin(SimpleHistoryAdmin):
    form = MetasForm
    list_display = ['codigo', 'nome', 'valor_meta', 'prazo', ]
    search_fields = ['codigo', 'nome', 'indicadores', 'valor_meta', ]
    date_hierarchy = 'prazo'
    filter_horizontal = ['necessidades', 'indicadores', ]
    readonly_fields = ['codigo', ]


@admin.register(Acao)
class AcaoAdmin(SimpleHistoryAdmin):
    form = AcaoForm
    list_display = ['codigo', 'nome', 'data_inicio_estimada', 'data_conclusao_estimada']
    search_fields = ['codigo', 'nome',]
    date_hierarchy = 'data_conclusao_estimada'
    filter_horizontal = ['metas', 'areas_responsaveis', 'competencias']
    fieldsets = [
        (
            None,
            {
                'fields': [
                    ('codigo','nome'),
                    ('metas',),
                    ('areas_responsaveis',)
                ]
            },
        ),
        (
            'Prazos',
            {
                'fields': [
                    ('data_inicio_estimada','data_conclusao_estimada', ),
                ]
            },
        ),
        (
            'Recursos Humanos',
            {
                'fields': [
                    ('quantidade_pessoas',),
                    ('competencias', ),
                ]
            },
        ),
        (
            'Recursos Orçamentários',
            {
                'fields': [
                    ('valor_investimento', 'valor_custeio', ),
                ]
            },
        ),
    ]
    readonly_fields = ['codigo', ]
