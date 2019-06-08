from django.db import models
from apps.funcionarios.models import Funcionario
from apps.empresas.models import Empresa


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    proprietario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)


    def __str__(self):
        return self.descricao
    

