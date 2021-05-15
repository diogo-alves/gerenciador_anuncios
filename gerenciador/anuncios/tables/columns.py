from django.utils.formats import number_format

import django_tables2 as tables


class DecimalColumn(tables.Column):
    """
    Exibe o valor da coluna em formato decimal de acordo a configuração
    de localização do django.
    """

    def render(self, value):
        return number_format(value, use_l10n=True, force_grouping=True)
