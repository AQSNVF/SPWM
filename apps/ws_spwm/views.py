from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionario
from .tasks import send_relatorio


    # DjangoRest

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apps.ws_spwm.serializers import UserSerializer, GroupSerializer


@login_required()
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'ws_spwm/index.html', data)


def celery(request):
    send_relatorio.delay()
    return HttpResponse('SPWM incluiu esta tarefa na fila para execução')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

