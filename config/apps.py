from django.contrib.admin.apps import AdminConfig


class PdticAdminConfig(AdminConfig):
    default_site = 'config.admin.PdticAdminSite'
