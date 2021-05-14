from http import HTTPStatus

from django.urls import reverse
from django.test import TestCase

from ..models import Anuncio, Cliente


class ClienteCreateViewTests(TestCase):

    def setUp(self):
        self.url = reverse('anuncios:cliente_create')

    def test_template_utilizado(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'anuncios/cliente_create.html')

    def test_resposta_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_redirecionamento_apos_criacao(self):
        response = self.client.post(self.url, data={'nome': 'Cliente1'}, follow=True)
        cliente = response.context.get('cliente')
        self.assertEqual(Cliente.objects.count(), 1)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertRedirects(response, reverse('anuncios:cliente_detail', kwargs={'pk': cliente.pk}))

    def test_redirecionamento_apos_clicar_em_salvar_e_adicionar_outro(self):
        dados_cliente = {
            'nome': 'Anúncio 1',
            'btn_salvar_e_adicionar_outro': ''
        }
        response = self.client.post(self.url, data=dados_cliente)
        self.assertEqual(Cliente.objects.count(), 1)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('anuncios:cliente_create'))


class ClienteDetailViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.cliente = Cliente.objects.create(nome='Cliente 1')

    def setUp(self):
        self.url = reverse('anuncios:cliente_detail', kwargs={'pk': self.cliente.pk})

    def test_template_utilizado(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'anuncios/cliente_detail.html')

    def test_resposta_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class ClienteUpdateViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.cliente = Cliente.objects.create(nome='Cliente 1')

    def setUp(self):
        self.url = reverse('anuncios:cliente_update', kwargs={'pk': self.cliente.pk})

    def test_template_utilizado(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'anuncios/cliente_update.html')

    def test_resposta_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_redirecionamento_apos_edicao(self):
        dados_cliente = {'nome': 'Novo nome do cliente'}
        response = self.client.post(self.url, data=dados_cliente)
        cliente_atualizado = Cliente.objects.get(pk=self.cliente.pk)
        self.assertEqual(cliente_atualizado.nome, dados_cliente['nome'])
        self.assertRedirects(response, reverse('anuncios:cliente_detail', kwargs={'pk': self.cliente.pk}))
        self.assertEqual(Cliente.objects.count(), 1)


class ClienteDeleteViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.cliente = Cliente.objects.create(nome='Cliente 1')

    def setUp(self):
        self.url = reverse('anuncios:cliente_delete', kwargs={'pk': self.cliente.pk})

    def test_exclusao_de_objeto(self):
        response = self.client.post(self.url)
        self.assertEqual(Cliente.objects.count(), 0)
        self.assertRedirects(response, reverse('anuncios:cliente_list'))


class ClienteListViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Cliente.objects.bulk_create([
            Cliente(nome='Cliente 1'),
            Cliente(nome='Cliente 2'),
        ])

    def setUp(self):
        self.url = reverse('anuncios:cliente_list')

    def test_template_utilizado(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'anuncios/cliente_list.html')

    def test_resposta_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_quantidade_de_objetos_retornados(self):
        response = self.client.get(self.url)
        object_list = response.context.get('object_list')
        self.assertEqual(len(object_list), 2)


class AnuncioCreateViewTests(TestCase):

    def setUp(self):
        self.url = reverse('anuncios:anuncio_create')

    def test_templates_utilizados(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'anuncios/anuncio_create.html')
        self.assertTemplateUsed(response, 'anuncios/_anuncio_form_fields.html')

    def test_resposta_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_redirecionamento_apos_criacao(self):
        cliente = Cliente.objects.create(nome='Cliente 1')
        dados_anuncio = {
            'nome': 'Anúncio 1',
            'cliente': cliente.pk,
            'data_inicio': '2021-05-01',
            'data_termino': '2021-05-31',
            'investimento_diario': '5000'
        }
        response = self.client.post(self.url, data=dados_anuncio, follow=True)
        anuncio = response.context.get('anuncio')
        self.assertEqual(Anuncio.objects.count(), 1)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertRedirects(response, reverse('anuncios:anuncio_detail', kwargs={'pk': anuncio.pk}))

    def test_redirecionamento_apos_clicar_em_salvar_e_adicionar_outro(self):
        cliente = Cliente.objects.create(nome='Cliente 1')
        dados_anuncio = {
            'nome': 'Anúncio 1',
            'cliente': cliente.pk,
            'data_inicio': '2021-05-01',
            'data_termino': '2021-05-31',
            'investimento_diario': '5000',
            'btn_salvar_e_adicionar_outro': ''
        }
        response = self.client.post(self.url, data=dados_anuncio)
        self.assertEqual(Anuncio.objects.count(), 1)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('anuncios:anuncio_create'))


class AnuncioDetailViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cliente = Cliente.objects.create(nome='Cliente 1')
        cls.anuncio = Anuncio.objects.create(
            nome='Anúncio 1',
            cliente=cliente,
            data_inicio='2021-05-01',
            data_termino='2021-05-31',
            investimento_diario=5000.00
        )

    def setUp(self):
        self.url = reverse('anuncios:anuncio_detail', kwargs={'pk': self.anuncio.pk})

    def test_template_utilizado(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'anuncios/anuncio_detail.html')

    def test_resposta_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class AnuncioUpdateViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.cliente = Cliente.objects.create(nome='Cliente 1')
        cls.anuncio = Anuncio.objects.create(
            nome='Anúncio 1',
            cliente=cls.cliente,
            data_inicio='2021-05-01',
            data_termino='2021-05-31',
            investimento_diario=5000.00
        )

    def setUp(self):
        self.url = reverse('anuncios:anuncio_update', kwargs={'pk': self.anuncio.pk})

    def test_templates_utilizados(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'anuncios/anuncio_update.html')
        self.assertTemplateUsed(response, 'anuncios/_anuncio_form_fields.html')

    def test_resposta_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_redirecionamento_apos_edicao(self):
        dados_anuncio = {
            'nome': 'Anúncio editado',
            'cliente': self.cliente.pk,
            'data_inicio': '2021-05-01',
            'data_termino': '2021-05-31',
            'investimento_diario': '5000',
        }
        response = self.client.post(self.url, data=dados_anuncio)
        anuncio_atualizado = Anuncio.objects.get(pk=self.anuncio.pk)
        self.assertEqual(anuncio_atualizado.nome, dados_anuncio['nome'])
        self.assertRedirects(response, reverse('anuncios:anuncio_detail', kwargs={'pk': self.anuncio.pk}))
        self.assertEqual(Anuncio.objects.count(), 1)


class AnuncioDeleteViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cliente = Cliente.objects.create(nome='Cliente 1')
        cls.anuncio = Anuncio.objects.create(
            nome='Anúncio 1',
            cliente=cliente,
            data_inicio='2021-05-01',
            data_termino='2021-05-31',
            investimento_diario=5000.00
        )

    def setUp(self):
        self.url = reverse('anuncios:anuncio_delete', kwargs={'pk': self.anuncio.pk})

    def test_exclusao_de_objeto(self):
        response = self.client.post(self.url)
        self.assertEqual(Anuncio.objects.count(), 0)
        self.assertRedirects(response, reverse('anuncios:anuncio_list'))


class AnuncioListViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cliente = Cliente.objects.create(nome='Cliente')
        Anuncio.objects.bulk_create([
            Anuncio(
                nome='Anúncio 1',
                cliente=cliente,
                data_inicio='2021-05-01',
                data_termino='2021-05-31',
                investimento_diario=5000.00
            ),
            Anuncio(
                nome='Anúncio 2',
                cliente=cliente,
                data_inicio='2021-04-01',
                data_termino='2021-05-01',
                investimento_diario=1000.00
            )
        ])

    def setUp(self):
        self.url = reverse('anuncios:anuncio_list')

    def test_template_utilizado(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'anuncios/anuncio_list.html')

    def test_resposta_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_quantidade_de_objetos_retornados(self):
        response = self.client.get(self.url)
        object_list = response.context.get('object_list')
        self.assertEqual(len(object_list), 2)
