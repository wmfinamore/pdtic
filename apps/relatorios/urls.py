from django.urls import path
from .views import ProjetoPdf


urlpatterns = [
    path('projeto/<int:id>', ProjetoPdf.as_view(), name='projeto'),
]
