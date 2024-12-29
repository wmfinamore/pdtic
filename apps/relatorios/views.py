from django.views import View
from .process import Render
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.projetos.models import Projeto, Fase


class ProjetoPdf(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        data = Projeto.projetos_ativos.get(id=id)
        protocolo = request.META['SERVER_PROTOCOL'][:5]
        if protocolo != 'HTTPS':
            protocolo = 'http://'
        else:
            protocolo = 'https://'
        params = {
            'Projeto': data,
            'HOST': protocolo + request.META['HTTP_HOST']
        }
        return Render.render('relatorios/projeto.html',
                             params,
                             f"Projeto_{data.id}")
