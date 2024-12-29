from django.urls import path
from .views import SecretariasListView
from django.views.decorators.cache import cache_page
from config.settings import CUSTOM_CACHE_TIME
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',
         login_required(
            cache_page(CUSTOM_CACHE_TIME)(SecretariasListView.as_view())
        ), name='lista_secretaria'),
]
