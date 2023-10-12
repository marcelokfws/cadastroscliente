
from django.db import models


class Cracha(models.Model):

    nome = models.CharField(max_length=100)
    foto = models.FileField()

    class Meta:
        verbose_name = ("cadastro")
        verbose_name_plural = ("cadastros")

    def __str__(self):
        return self.nome
