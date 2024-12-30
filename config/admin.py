from django.contrib.admin import AdminSite



class PdticAdminSite(AdminSite):
    site_header = 'Gestão do Plano Diretor de TECNOLOGIA DA INFORMAÇÃO E COMUNICAÇÃO'
    site_title = 'PDTIC'
    index_title = 'Administração'
    site_url = '/pdtic'

    def get_urls(self):
        urls = super().get_urls()
        return urls
