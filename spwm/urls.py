from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('apps.ws_spwm.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('admin/', admin.site.urls),
]

