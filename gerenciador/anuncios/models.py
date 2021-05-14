import uuid
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

from .utils import (
    calcula_alcance_anuncio,
    converte_views_em_cliques,
    converte_cliques_em_compartilhamentos,
)


class Cliente(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = 'cliente'
        ordering = ['nome']

    def __str__(self) -> str:
        """Retorna a representação textual do cliente"""
        return self.nome

    def get_absolute_url(self) -> str:
        """Retorna a url para a página que detalha o cliente"""
        return reverse('anuncios:cliente_detail', kwargs={'pk': self.id})


class Anuncio(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    nome = models.CharField(max_length=200)
    cliente = models.ForeignKey(
        to=Cliente,
        on_delete=models.CASCADE,
        related_name='anuncios'
    )
    data_inicio = models.DateField(verbose_name='data de início')
    data_termino = models.DateField(verbose_name='data de término')
    investimento_diario = models.DecimalField(
        verbose_name='investimento diário',
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        db_table = 'anuncio'
        ordering = ['-data_inicio', '-data_termino']
        verbose_name = 'anúncio'
        verbose_name_plural = 'anúncios'

    def __str__(self) -> str:
        """Retorna a representação textual do anúncio"""
        return self.nome

    def get_absolute_url(self) -> str:
        """Retorna a url para a página que detalha o anúncio"""
        return reverse('anuncios:anuncio_detail', kwargs={'pk': self.id})

    def clean(self) -> None:
        """Realiza validações entre campos do model"""
        if self.data_inicio and self.data_termino and self.data_inicio > self.data_termino:
            raise ValidationError('A data de início não deve ser maior que a data de término do anúncio.')

    @property
    def dias_ativo(self) -> int:
        """Retorna a quantidade de dias que o anúncio ficará ativo"""
        return (self.data_termino - self.data_inicio).days + 1

    @property
    def total_investido(self) -> Decimal:
        """
        Retorna o valor total investido de acordo com a quantidade de
        dias em que o anúncio esteve ativo
        """
        return self.investimento_diario * self.dias_ativo

    @property
    def visualizacoes(self) -> int:
        """Retorna a quantidade máxima de visualizações do anúncio"""
        visualizacoes = calcula_alcance_anuncio(self.total_investido)
        return int(visualizacoes)

    @property
    def cliques(self) -> int:
        """Retorna a quantidade máxima de cliques do anúncio"""
        cliques = converte_views_em_cliques(self.visualizacoes)
        return int(cliques)

    @property
    def compartilhamentos(self) -> int:
        """Retorna a quantidade máxima de compartilhamentos do anúncio"""
        compartilhamentos = converte_cliques_em_compartilhamentos(self.cliques)
        return int(compartilhamentos)
