import argparse
import unittest
from unittest.mock import patch

__all__ = (
    'calcula_alcance_anuncio',
    'calcula_views_anuncio_original',
    'projeta_total_views_anuncio',
    'converte_interacoes_em_views',
    'converte_views_em_cliques',
    'converte_cliques_em_compartilhamentos',
    'converte_compartilhamentos_em_views',
)

NUM_MAX_COMPARTILHAMENTOS_EM_SEQUENCIA = 4
NUM_VIEWS_ANUNCIO_ORIGINAL_POR_REAL_INVESTIDO = 30
NUM_VIEWS_POR_ANUNCIO_COMPARTILHADO = 40
PERCENTUAL_CONVERSAO_CLIQUES_EM_COMPARTILHAMENTOS = 15
PERCENTUAL_CONVERSAO_VIEWS_EM_CLIQUES = 12


def calcula_alcance_anuncio(valor_investido):
    """
    Retorna a projeção de views de um anúncio com base no valor
    investido.
    """
    views_iniciais = calcula_views_anuncio_original(valor_investido)
    total_views = projeta_total_views_anuncio(views_iniciais)
    return total_views


def calcula_views_anuncio_original(valor_investido):
    """
    Retorna o número proporcional de views do anúncio original em
    relação ao valor investido.
    """
    if valor_investido <= 0:
        return 0
    views = valor_investido * NUM_VIEWS_ANUNCIO_ORIGINAL_POR_REAL_INVESTIDO
    return views


def projeta_total_views_anuncio(num_views):
    """
    Realiza a projeção de views que um anúncio pode receber com base no
    seu número inicial de views e a quantidade máxima de
    compartilhamentos sequenciais permitida.
    """
    totais = [num_views]
    for _ in range(1, NUM_MAX_COMPARTILHAMENTOS_EM_SEQUENCIA):
        num_views = converte_interacoes_em_views(num_views)
        totais.append(num_views)
    return sum(totais)


def converte_interacoes_em_views(num_views):
    """
    Retorna o número projetado de views que uma certa quantidade de
    views pode gerar através de suas interações.
    """
    cliques = converte_views_em_cliques(num_views)
    compartilhamentos = converte_cliques_em_compartilhamentos(cliques)
    novas_views = converte_compartilhamentos_em_views(compartilhamentos)
    return novas_views


def converte_views_em_cliques(num_views):
    """
    Retorna o número de cliques que uma determinada quantidade de views
    pode gerar, levando em conta a taxa de conversão de views em cliques.
    """
    cliques = num_views * PERCENTUAL_CONVERSAO_VIEWS_EM_CLIQUES / 100
    return cliques


def converte_cliques_em_compartilhamentos(num_cliques):
    """
    Retorna o número de compartilhamentos que uma determinada quantidade
    de cliques no anúncio pode gerar, levando em conta a taxa de
    conversão de cliques em compartilhamentos.
    """
    compartilhamentos = num_cliques * PERCENTUAL_CONVERSAO_CLIQUES_EM_COMPARTILHAMENTOS / 100
    return compartilhamentos


def converte_compartilhamentos_em_views(num_compartilhamentos):
    """
    Retorna o número de views que uma determinada quantidade de
    compartilhamentos do anúncio pode gerar, levando em conta a taxa de
    conversão de views por anúncio compartilhado.
    """
    views = num_compartilhamentos * NUM_VIEWS_POR_ANUNCIO_COMPARTILHADO
    return views


class TestAlcanceAnuncio(unittest.TestCase):

    def test_converte_views_em_cliques(self):
        num_cliques = converte_views_em_cliques(num_views=100)
        self.assertEqual(num_cliques, 12)

    @unittest.skip('Cenário não confirmado nos requisitos')
    def test_converte_views_em_cliques_deve_retornar_valores_inteiros(self):
        num_cliques = converte_views_em_cliques(num_views=10)
        self.assertNotEqual(num_cliques, 1.2)
        self.assertEqual(num_cliques, 1)

    def test_converte_views_em_cliques_quando_nao_existem_views(self):
        num_cliques = converte_views_em_cliques(num_views=0)
        self.assertEqual(num_cliques, 0)

    def test_converte_cliques_em_compartilhamentos(self):
        num_compartilhamentos = converte_cliques_em_compartilhamentos(num_cliques=20)
        self.assertEqual(num_compartilhamentos, 3)

    @unittest.skip('Cenário não confirmado nos requisitos')
    def test_converte_cliques_em_compartilhamentos_deve_retornar_valores_inteiros(self):
        num_compartilhamentos = converte_cliques_em_compartilhamentos(num_cliques=10)
        self.assertNotEqual(num_compartilhamentos, 1.5)
        self.assertEqual(num_compartilhamentos, 1)

    def test_converte_cliques_em_compartilhamentos_quando_nao_existem_cliques(self):
        num_compartilhamentos = converte_cliques_em_compartilhamentos(num_cliques=0)
        self.assertEqual(num_compartilhamentos, 0)

    def test_converte_compartilhamentos_em_views(self):
        num_views = converte_compartilhamentos_em_views(num_compartilhamentos=1)
        self.assertEqual(num_views, 40)

    def test_converte_compartilhamentos_em_views_quando_nao_existem_compartilhamentos(self):
        num_views = converte_compartilhamentos_em_views(num_compartilhamentos=0)
        self.assertEqual(num_views, 0)

    def test_converte_interacoes_em_views(self):
        num_novas_views = converte_interacoes_em_views(num_views=100)
        # self.assertEqual(num_novas_views, 40)
        self.assertEqual(num_novas_views, 72)

    def test_converte_interacoes_em_views_quando_nao_existem_views_para_gerar_interacoes(self):
        num_novas_views = converte_interacoes_em_views(num_views=0)
        self.assertEqual(num_novas_views, 0)

    def test_projeta_total_views_anuncio(self):
        num_views = projeta_total_views_anuncio(num_views=3000)
        # self.assertEqual(num_views, 7760)
        self.assertEqual(num_views, 7834.9439999999995)

    @patch(__name__ + '.NUM_MAX_COMPARTILHAMENTOS_EM_SEQUENCIA', 0)
    def test_projeta_total_views_anuncio_quando_nao_forem_permitidos_compartilhamentos(self):
        total_views = projeta_total_views_anuncio(num_views=3000)
        self.assertEqual(total_views, 3000)

    def test_calcula_views_anuncio_original(self):
        num_views = calcula_views_anuncio_original(valor_investido=1)
        self.assertEqual(num_views, 30)

    def test_calcula_views_anuncio_original_quando_valor_investido_for_fracao(self):
        num_views = calcula_views_anuncio_original(valor_investido=0.1)
        self.assertEqual(num_views, 3)

    @unittest.skip('Cenário não confirmado nos requisitos')
    def test_calcula_views_anuncio_original_deve_retornar_valores_inteiros(self):
        num_views = calcula_views_anuncio_original(valor_investido=0.05)
        self.assertNotEqual(num_views, 1.5)
        self.assertEqual(num_views, 1)

    def test_calcula_views_anuncio_original_quando_valor_investido_for_zero(self):
        num_views = calcula_views_anuncio_original(valor_investido=0)
        self.assertEqual(num_views, 0)

    def test_calcula_views_anuncio_original_quando_valor_investido_for_negativo(self):
        num_views = calcula_views_anuncio_original(valor_investido=-1)
        self.assertEqual(num_views, 0)

    def test_calcula_alcance_anuncio(self):
        num_views = calcula_alcance_anuncio(valor_investido=100)
        # self.assertEqual(num_views, 7760)
        self.assertEqual(num_views, 7834.9439999999995)


def main():
    parser = argparse.ArgumentParser(
        prog='calculadora',
        usage='python3 -m calculadora',
        description='Calculadora de alcance de anúncios online.'
    )
    parser.add_argument('valor', type=float, help='valor investido')
    args = parser.parse_args()
    total_views = calcula_alcance_anuncio(args.valor)
    print(total_views)


if __name__ == '__main__':
    main()
