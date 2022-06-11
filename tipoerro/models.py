from django.db import models


class TipoErro(models.Model):

    descricao_erro = models.CharField(max_length=200)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao_erro

    class Meta:
        db_table = "tipoerro"
        verbose_name_plural = "TiposErros"
        ordering = ['descricao_erro']
