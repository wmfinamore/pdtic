from django.contrib.admin import AdminSite


class PdticAdminSite(AdminSite):
    site_header = 'Gestão do Plano Diretor de Tecnologia da Informação e Comunicação'
    site_title = 'PDTIC'
    index_title = 'Administração'
    site_url = '/pdtic'

    def get_urls(self):
        urls = super().get_urls()
        return urls
