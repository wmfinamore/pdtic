from django.views.generic import TemplateView
from django.shortcuts import redirect


class HomeView(TemplateView):
    template_name = 'core/home.html'


def redirect_view(request):
    response = redirect('/pdtic/')
    return response
