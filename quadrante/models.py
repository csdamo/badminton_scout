from django.db import models


class Quadrante(models.Model):

    SIDE_CHOICES = (
        ('esquerdo', 'Esquerdo'),
        ('direito', 'Direito'),
    )

    descricao_quadrante = models.CharField(max_length=100)

    lado = models.CharField(
        max_length=9,
        choices=SIDE_CHOICES,
        default='esquerdo',
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        quadrante = self.descricao_quadrante
        lado = self.lado
        return f'Q: {quadrante} - lado {lado}'

    class Meta:
        db_table = "quadrante"
        verbose_name_plural = "Quadrantes"
        ordering = ['descricao_quadrante']
