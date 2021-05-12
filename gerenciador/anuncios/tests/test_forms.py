from django.test import TestCase

from ..forms import AnuncioForm, ClienteForm
from ..models import Anuncio, Cliente


class ClienteFormTest(TestCase):

    def test_model_utilizado(self):
        form = ClienteForm()
        self.assertEqual(form._meta.model, Cliente)

    def test_campos_utilizados(self):
        form = ClienteForm()
        self.assertEqual(list(form.base_fields), ['nome'])

    def test_campo_obrigatorio(self):
        form = ClienteForm()
        self.assertTrue(form.fields['nome'].required)


class AnuncioFormTest(TestCase):

    def test_model_utilizado(self):
        form = AnuncioForm()
        self.assertEqual(form._meta.model, Anuncio)

    def test_campos_utilizados(self):
        form = AnuncioForm()
        fields = [
            'nome',
            'cliente',
            'data_inicio',
            'data_termino',
            'investimento_diario',
        ]
        self.assertEqual(list(form.base_fields), fields)

    def test_campos_obrigatorios(self):
        form = AnuncioForm()
        self.assertTrue(form.fields['nome'].required)
        self.assertTrue(form.fields['cliente'].required)
        self.assertTrue(form.fields['data_inicio'].required)
        self.assertTrue(form.fields['data_termino'].required)
        self.assertTrue(form.fields['investimento_diario'].required)
