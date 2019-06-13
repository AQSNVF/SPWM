from django.db import models
from django.shortcuts import reverse

from apps.funcionarios.models import Funcionario
from apps.empresas.models import Empresa


class DocumentoFunc(models.Model):
    descricao = models.CharField(max_length=100)
    proprietariofunc = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentosfunc')

    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.proprietariofunc.id])

    def __str__(self):
        return self.descricao
    

