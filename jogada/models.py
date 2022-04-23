from django.db import models

from set.models import Set
from golpe.models import Golpe
from jogador.models import Jogador
from quadrante.models import Quadrante


class Jogada(models.Model):

    TIPO_STATUS_CHOICES = (
        ('acerto', 'Acerto'),
        ('erro', 'Erro'),
        ('normal', 'Normal'),
    )

    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    golpe = models.ForeignKey(Golpe, on_delete=models.CASCADE)
    quadrante = models.ForeignKey(Quadrante, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=6,
        choices=TIPO_STATUS_CHOICES,
        default='normal',
    )

    ponto_jogador = models.PositiveIntegerField(default=0)
    ponto_jogador_adversario = models.PositiveIntegerField(default=0)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        cod = self.pk
        status = self.status
        jogador = self.jogador
        golpe = self.golpe
        return f'Jogada código {cod} - Jogador: {jogador} - Golpe: {golpe} - Status: {status}'

    class Meta:
        db_table = "jogada"
        verbose_name_plural = "Jogadas"
        ordering = ['set']
