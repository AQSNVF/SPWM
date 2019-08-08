from django.db import models


class WPS(models.Model):
    descricao = models.CharField(max_length=100)
    Produto = models.CharField(max_length=100)