
from django.db import models


class Cracha(models.Model):

    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    reds = models.CharField(max_length=255)
    foto = models.FileField()

    class Meta:
       
        verbose_name = ("cadastro")
        verbose_name_plural = ("cadastros")

    def __str__(self):
        return self.nome
