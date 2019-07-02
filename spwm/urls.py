from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls
    # DjangoRest
from rest_framework import routers
from apps.spwm_ws import views
from apps.funcionarios.api.views import FuncionarioViewSet
from apps.registro_hora_extra.api.views import RegistroHoraExtraViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'api/funcionarios', FuncionarioViewSet)
router.register(r'api/banco-horas', RegistroHoraExtraViewSet)


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('', include('apps.spwm_ws.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('empresa/', include('apps.empresas.urls')),
    path('documentosfunc/', include('apps.documentosfunc.urls')),
    path('horas-extras/', include('apps.registro_hora_extra.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # DjangoRest
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
