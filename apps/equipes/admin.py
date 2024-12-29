from django.contrib import admin
from .models import TipoCompetencia, Competencia, Desenvolvedor, NivelCompetencia,InventarioCompetencia
from .forms import (TipoCompetenciaoForm, CompetenciaoForm, DesenvolvedorForm, NivelCompetenciaForm,
                    InventarioCompetenciaForm)
from simple_history.admin import SimpleHistoryAdmin


@admin.register(TipoCompetencia)
class TipoCompetenciaAdmin(SimpleHistoryAdmin):
    form = TipoCompetenciaoForm
    list_display = ['id', 'tipo_competencia']
    search_fields = ['tipo_competencia', 'descricao', ]
    list_display_links = ['tipo_competencia']


class InventarioCompetenciaAdminInLine(admin.StackedInline):
    model = InventarioCompetencia
    form = InventarioCompetenciaForm
    fieldsets = (
        (None, {
            'fields': (
                ('competencia', 'nivel'),
            )
        }),
        ("Detalhes da Competência", {
            'classes': ('collapse',),
            'fields': (
                ('aquisicao_competencia',),
                ('data_alteracao', 'hora_alteracao'),
            )
        })
    )
    extra = 0
    readonly_fields = ['data_alteracao', 'hora_alteracao', ]
    autocomplete_fields = ['competencia', 'nivel', ]


@admin.register(Competencia)
class CompetenciaAdmin(SimpleHistoryAdmin):
    form = CompetenciaoForm
    list_display = ['id', 'competencia', 'tipo_competencia', ]
    search_fields = ['descricao', ]
    list_display_links = ['competencia']
    list_filter = ['tipo_competencia', ]
    list_select_related = ['tipo_competencia', ]


@admin.register(Desenvolvedor)
class DesenvolvedorAdmin(SimpleHistoryAdmin):
    form = DesenvolvedorForm
    list_display = ['matricula', 'nome', 'email', 'ativo']
    search_fields = ['nome', 'email', 'matricula', ]
    list_display_links = ['nome',]
    list_filter = ['ativo']
    inlines = [InventarioCompetenciaAdminInLine, ]


@admin.register(NivelCompetencia)
class NivelCompetenciaAdmin(SimpleHistoryAdmin):
    form = NivelCompetenciaForm
    list_display = ['id', 'nivel', 'descricao', ]
    search_fields = ['nivel', 'descricao', ]
    list_display_links = ['nivel',]


@admin.register(InventarioCompetencia)
class InventarioCompetenciaAdmin(SimpleHistoryAdmin):
    form = InventarioCompetenciaForm
    list_display = ['desenvolvedor', 'competencia', 'nivel', ]
    search_fields = ['desenvolvedor__nome', 'competencia__competencia', 'nivel__nivel', ]
    list_filter = ['desenvolvedor', 'competencia', 'nivel']
