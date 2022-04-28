from django.db import models

from partida.models import Partida


class Set(models.Model):

    partida = models.ForeignKey(Partida, on_delete=models.PROTECT)
    ordem = models.PositiveSmallIntegerField()

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        cod = str(self.pk)
        ordem = self.ordem
        partida = self.partida
        return f'Set código {cod} - ordem {ordem}º - Partida: {partida}'

    class Meta:
        db_table = "set"
        verbose_name_plural = "Sets"
        ordering = ['partida', 'ordem']
