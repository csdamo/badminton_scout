from django.db import models


class Jogador(models.Model):

    TIPO_LATERALIDADE_CHOICES = (
        ('destro', 'Destro'),
        ('canhoto', 'Canhoto'),
        ('ambidestro', 'Ambidestro'),
        ('naoinformado', 'Não informado'),
    )

    nome_jogador = models.CharField(max_length=200)
    data_nascimento = models.DateField(blank=True, null=True)
    telefone = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)

    lateralidade = models.CharField(
        max_length=12,
        choices=TIPO_LATERALIDADE_CHOICES,
        default='naoinformado',
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_jogador

    class Meta:
        db_table = "jogador"
        verbose_name_plural = "Jogadores"
        ordering = ['nome_jogador']
