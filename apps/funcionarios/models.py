from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from django.db.models import Sum

from django.core.mail import send_mail


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    cpf = models.CharField(max_length=100, null=False, blank=False)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, null=True, blank=True)
    imagem = models.ImageField()
    de_ferias = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('list_funcionarios')


    @property
    def total_horas_extra(self):
        total = self.registrohoraextra_set.filter(
            utilizada=False).aggregate(
            Sum('horas'))['horas__sum']
        return total or 0


    def save(self, *args, **kwargs):
        super(Funcionario, self).save(*args, **kwargs)

        send_mail(
            'Novo Funcionário Cadastrado teste 2 emails',
            'O Funcionário %s foi cadastrado no SPWM' % self.nome,
            'nelson.freire@ativa-qs.com.br',
            ['nelson.freire@ativa-qs.com.br', 'nelson.freire@spwm.com.br'],
            fail_silently=False
        )


    def __str__(self):
        return self.nome


