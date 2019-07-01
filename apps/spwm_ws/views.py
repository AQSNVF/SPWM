from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.departamentos.models import Departamento
from apps.spwm_ws import serializers
from django.core import serializers
from django.http import HttpResponse

from apps.funcionarios.models import Funcionario
from apps.registro_hora_extra.models import RegistroHoraExtra

from .tasks import send_relatorio


    # DjangoRest

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apps.spwm_ws.serializers import UserSerializer, GroupSerializer


@login_required()
def home(request):
    data = {}
    data['usuario'] = request.user
    funcionario = request.user.funcionario
    data['total_funcionarios'] = Funcionario.objects.all().count()
    data['total_funcionarios_ferias'] = funcionario.empresa.total_funcionarios_ferias
    data['total_funcionarios_doc_pendentes'] = funcionario.empresa.total_funcionarios_doc_pendentes
    data['total_funcionarios_doc_ok'] = funcionario.empresa.total_funcionarios_doc_ok
    data['total_funcionarios_cpf'] = Funcionario.objects.all().count()
    data['total_hora_extra'] = (
             RegistroHoraExtra.objects.filter(
             funcionario__empresa=funcionario.empresa, utilizada=True).aggregate(
                 Sum('horas'))['horas__sum']) + (
             RegistroHoraExtra.objects.filter(
             funcionario__empresa=funcionario.empresa, utilizada=False).aggregate(
                 Sum('horas'))['horas__sum'])
    data['total_hora_extra_utilizadas'] = RegistroHoraExtra.objects.filter(
        funcionario__empresa=funcionario.empresa, utilizada=True).aggregate(Sum('horas'))['horas__sum']
    data['total_hora_extra_pendentes'] = RegistroHoraExtra.objects.filter(
        funcionario__empresa=funcionario.empresa, utilizada=False).aggregate(Sum('horas'))['horas__sum']

    return render(request, 'spwm_ws/index.html', data)


def celery(request):
    send_relatorio()
    return HttpResponse('SPWM incluiu esta tarefa na fila na maquina 25 / 06 -  -')


def departamentos_ajax(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos_ajax.html', {'departamentos': departamentos})

def filtra_funcionarios(request):

    depart = request.GET['outro_param']
    departamento = Departamento.objects.get(id=depart)

    qs_json = serializers.serialize('json', departamento.funcionario_set.all())
    return HttpResponse(qs_json, content_type='application/json')


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

