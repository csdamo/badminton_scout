from django.db import models

from set.models import Set
from golpe.models import Golpe
from jogador.models import Jogador
from quadrante.models import Quadrante


class Jogada(models.Model):

    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE, blank=True, null=True)
    golpe = models.ForeignKey(Golpe, on_delete=models.CASCADE)
    quadrante = models.ForeignKey(Quadrante, on_delete=models.CASCADE)

    acerto = models.BooleanField()

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        cod = self.pk
        acerto = self.acerto
        golpe = self.golpe
        return f'Jogada código {cod} - Golpe: {golpe} - Status: {acerto}'

    class Meta:
        db_table = "jogada"
        verbose_name_plural = "Jogadas"
        ordering = ['set']
