from django import forms

from .models import Anuncio, Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nome']


class AnuncioForm(forms.ModelForm):

    class Meta:
        model = Anuncio
        fields = [
            'nome',
            'cliente',
            'data_inicio',
            'data_termino',
            'investimento_diario',
        ]
