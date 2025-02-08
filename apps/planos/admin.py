from django.contrib import admin
from .models import PrincipioDiretriz, FonteDiretriz
from .forms import PrincipioDiretrizForm, FonteDiretrizForm
from simple_history.admin import SimpleHistoryAdmin


@admin.register(FonteDiretriz)
class FonteDiretrizAdmin(SimpleHistoryAdmin):
    form = FonteDiretrizForm
    model = FonteDiretriz
    list_filter = ['id', 'nome', ]
    search_fields = ['nome', ]


@admin.register(PrincipioDiretriz)
class PrincipioDiretrizAdmin(SimpleHistoryAdmin):
    form = PrincipioDiretrizForm
    model = PrincipioDiretriz
    list_display = ['codigo', 'principio_diretriz', 'origem', 'criterio_priorizacao',]
    search_fields = ['codigo', 'principio_diretriz', 'origem', ]
    list_filter = ['origem', 'criterio_priorizacao',]
    fieldsets = (
        (None, {
            'fields': (
                ('codigo',),
                ('principio_diretriz',),
                ('origem', 'criterio_priorizacao'),
            )
        }),
    )
    autocomplete_fields = ['origem', ]
    readonly_fields = ['codigo', ]
