from django.db import models

from jogador.models import Jogador


class Partida(models.Model):

    TIPO_PARTIDA_CHOICES = (
        ('simples', 'Simples'),
        ('dupla', 'Dupla'),
    )

    MODALIDADE_CHOICES = (
        ('feminino', 'Feminino'),
        ('masculino', 'Masculino'),
        ('misto', 'Misto'),
    )

    data_partida = models.DateTimeField()

    tipo_jogo = models.CharField(
        max_length=7,
        choices=TIPO_PARTIDA_CHOICES,
        default='simples',
    )

    modalidade = models.CharField(
        max_length=9,
        choices=MODALIDADE_CHOICES,
        default='misto',
    )

    jogador_1 = models.ForeignKey(
        Jogador, on_delete=models.PROTECT, related_name='jogador_1')
    jogador_2 = models.ForeignKey(
        Jogador, on_delete=models.PROTECT, related_name='jogador_2', blank=True, null=True)

    jogador_adversario_1 = models.ForeignKey(
        Jogador, on_delete=models.PROTECT, related_name='jogador_adversario_1')
    jogador_adversario_2 = models.ForeignKey(
        Jogador, on_delete=models.PROTECT, related_name='jogador_adversario_2', blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        tipo_jogo = self.tipo_jogo
        data_partida = self.data_partida
        cod = str(self.pk)
        return f'partida cód {cod} - Data: {data_partida} - jogo {tipo_jogo}'

    class Meta:
        db_table = "partida"
        verbose_name_plural = "Partidas"
        ordering = ['data_partida']
