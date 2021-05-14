import django_tables2 as tables

from .models import Anuncio, Cliente


class ClienteTable(tables.Table):
    nome = tables.Column(linkify=True)

    class Meta:
        model = Cliente
        fields = ['nome']
        per_page = 5


class AnuncioTable(tables.Table):
    nome = tables.Column(linkify=True)

    class Meta:
        model = Anuncio
        fields = [
            'nome',
            'cliente',
            'data_inicio',
            'data_termino',
            'investimento_diario',
        ]
        per_page = 5
