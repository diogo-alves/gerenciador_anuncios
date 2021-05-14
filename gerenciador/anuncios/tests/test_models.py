from datetime import datetime, timedelta

from django.test import TestCase
from django.core.exceptions import ValidationError

from ..models import Anuncio, Cliente


class AnuncioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.anuncio = Anuncio.objects.create(
            nome='Aplicativo de consulta do FGTS',
            cliente=Cliente.objects.create(nome='Caixa'),
            data_inicio=datetime.now(),
            data_termino=datetime.now() + timedelta(days=4),
            investimento_diario=100
        )

    def test_str(self):
        self.assertEqual(str(self.anuncio), self.anuncio.nome)

    def test_foreignkey(self):
        self.assertIsInstance(self.anuncio.cliente, Cliente)

    def test_dias_ativo(self):
        self.assertEqual(self.anuncio.dias_ativo, 5)

    def test_total_investido(self):
        self.assertEqual(self.anuncio.total_investido, 500)

    def test_visualizacoes(self):
        self.assertEqual(self.anuncio.visualizacoes, 39174.72)

    def test_cliques(self):
        self.assertEqual(self.anuncio.cliques, 4700.9664)

    def test_compartilhamentos(self):
        self.assertEqual(self.anuncio.compartilhamentos, 705.14496)

    def test_nao_deve_haver_data_inicio_maior_que_data_final(self):
        mensagem_esperada = 'A data de início não deve ser maior que a data de término do anúncio.'
        with self.assertRaisesMessage(ValidationError, mensagem_esperada):
            anuncio = Anuncio.objects.create(
                nome='Aplicativo de consulta do FGTS',
                cliente=Cliente.objects.create(nome='Caixa'),
                data_inicio=datetime.now() + timedelta(days=1),
                data_termino=datetime.now(),
                investimento_diario=100
            )
            anuncio.full_clean()

    def test_investimento_nao_deve_ser_negativo(self):
        mensagem_esperada = 'Certifique-se que este valor seja maior ou igual a 0.'
        with self.assertRaisesMessage(ValidationError, mensagem_esperada):
            anuncio = Anuncio.objects.create(
                nome='Aplicativo de consulta do FGTS',
                cliente=Cliente.objects.create(nome='Caixa'),
                data_inicio=datetime.now(),
                data_termino=datetime.now(),
                investimento_diario=-0.01
            )
            anuncio.full_clean()
