from django_filters import FilterSet

from .models import Anuncio


class AnuncioFilter(FilterSet):

    class Meta:
        model = Anuncio
        fields = {
            'cliente': ['exact'],
            'data_inicio': ['gte'],
            'data_termino': ['lte'],
        }
