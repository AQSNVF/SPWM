from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from apps.funcionarios.models import Funcionario

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def send_relatorio():
    total = Funcionario.objects.all().count()
    send_mail(
        'Relatorio Celery',
        'Meu 1° relatorio de funcionarios por  25/06 maquina  -  %f' % total,
        'nelson.freire@ativa-qs.com.br',
        ['nelson.freire@spwm.com.br'],
        fail_silently=False,
    )

    return True
