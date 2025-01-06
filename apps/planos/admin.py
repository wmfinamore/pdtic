from django.contrib import admin
from .models import PrincipioDiretriz
from .forms import PrincipioDiretrizForm
from simple_history.admin import SimpleHistoryAdmin


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
                ('codigo', 'principio_diretriz'),
                ('origem', 'criterio_priorizacao'),
            )
        }),
    )
