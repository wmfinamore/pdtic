from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from apps.core.views import redirect_view


urlpatterns = [
    path('', redirect_view),
    path('pdtic/accounts/', include('django.contrib.auth.urls')),
    path('pdtic/', include('apps.core.urls')),
    path('pdtic/admin/', admin.site.urls),
    path('pdtic/secretarias/', include('apps.secretarias.urls')),
]

# Rota para ativar o debug toolbar quando do django estiver em modo debug
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__', include(debug_toolbar.urls))
                  ] + urlpatterns
