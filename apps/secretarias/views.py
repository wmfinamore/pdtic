from django.views.generic import ListView
from .models import Secretaria
from django.contrib.auth.mixins import LoginRequiredMixin


class SecretariasListView(LoginRequiredMixin, ListView):
    login_url = '/sgpm/accounts/login'
    model = Secretaria
    context_object_name = 'secretarias'

    def get_queryset(self):
        secretarias = self.request.user.secretarias.all()
        return secretarias
