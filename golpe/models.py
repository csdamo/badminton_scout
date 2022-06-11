from django.db import models

from tipoerro.models import TipoErro


class Golpe(models.Model):

    descricao_golpe = models.CharField(max_length=200)
    tipo_erro = models.ForeignKey(TipoErro, on_delete=models.CASCADE, blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao_golpe

    class Meta:
        db_table = "golpe"
        verbose_name_plural = "Golpes"
        ordering = ['descricao_golpe']
