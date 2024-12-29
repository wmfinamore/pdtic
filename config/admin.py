from django.contrib.admin import AdminSite
from apps.relatorios.urls import urlpatterns as relatorios


class PdticAdminSite(AdminSite):
    site_header = 'Gestão do Plano Diretor de TECNOLOGIA DA INFORMAÇÃO E COMUNICAÇÃO'
    site_title = 'Projetos de TI'
    index_title = 'Administração'
    site_url = '/pdtic'

    def get_urls(self):
        urls = super().get_urls()
        return relatorios + urls
