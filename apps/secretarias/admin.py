from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Secretaria


class SecretariaAdmin(SimpleHistoryAdmin):
    list_display = ['sigla', 'nome']
    search_fields = ['sigla', 'nome']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        data = []
        # campos to tipo ManyToMany são Managers, sendo acessados pelos mesmos métodos
        secretarias = request.user.secretarias.all()
        for secretaria in secretarias:
            data.append(secretaria.sigla)
        if request.user.is_superuser:
            return qs
        return qs.filter(sigla__in=data)


admin.site.register(Secretaria, SecretariaAdmin)
