from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from django.db.models import Sum

from django.core.mail import send_mail, mail_admins, send_mass_mail
from django.template.loader import render_to_string

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

        data = {'funcionario': self.nome}
        plain_text = render_to_string(
            'funcionarios/emails/novo_funcionario.txt', data)
        html_mail = render_to_string(
            'funcionarios/emails/novo_funcionario.html', data)
        
        send_mail(
            'Novo Funcionário Cadastrado no SPWM',
            plain_text,
            'nelson.freire@ativa-qs.com.br',
            ['nelson.freire@ativa-qs.com.br', 'nelson.freire@spwm.com.br'],
            html_message=html_mail,
            fail_silently=False
        )

        mail_admins(
            'Novo Funcionário Cadastrado',
            plain_text,

            html_message=html_mail,
            fail_silently=False
        )


        message1 = ('SPWM', 'Aproveite a promoção do SPWM', 'nelson.freire@spwm.com.br',
                    ['nelson.freire@ativa-qs.com.br',
                    'nelson.freire@spwm.com.br',
                    'wpativa01@outlook.com.br', ]
                    )
        message2 = ('SPWM', 'Aproveite a nova promoção do SPWM', 'nelson.freire@spwm.com.br',
        ['nelson.freire@ativa-qs.com.br',
         'nelson.freire@spwm.com.br',
         'wpativa01@outlook.com.br', ]
                    )
        send_mass_mail((message1, message2), fail_silently=False)

    def __str__(self):
        return self.nome



