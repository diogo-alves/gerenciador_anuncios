from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DetailView, UpdateView, DeleteView
)

from django_filters.views import FilterView
from django_tables2 import SingleTableMixin, SingleTableView

from .filters import AnuncioFilter
from .forms import AnuncioForm, ClienteForm
from .mixins import SuccessMessageDeletionMixin
from .models import Anuncio, Cliente
from .tables import AnuncioTable, ClienteTable


class ClienteCreateView(SuccessMessageMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    success_message = 'Cliente "%(nome)s" criado com sucesso!'
    template_name = 'anuncios/cliente_create.html'

    def get_success_url(self):
        url = super().get_success_url()
        if 'btn_salvar_e_adicionar_outro' in self.request.POST:
            url = reverse_lazy('anuncios:cliente_create')
        return url


class ClienteDetailView(SingleTableMixin, DetailView):
    model = Cliente
    table_class = AnuncioTable
    template_name = 'anuncios/cliente_detail.html'

    def get_table_data(self):
        return self.object.anuncios.all()

    def get_table_kwargs(self):
        return {'exclude': ('id', 'cliente')}


class ClienteUpdateView(SuccessMessageMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_message = 'Cliente "%(nome)s" alterado com sucesso!'
    template_name = 'anuncios/cliente_update.html'


class ClienteDeleteView(SuccessMessageDeletionMixin, DeleteView):
    model = Cliente
    form_class = ClienteForm
    success_message = 'Cliente "%(nome)s" excluído com sucesso!'
    success_url = reverse_lazy('anuncios:cliente_list')


class ClienteListView(SingleTableView):
    model = Cliente
    table_class = ClienteTable
    template_name = 'anuncios/cliente_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existem_objetos_cadastrados'] = self.model.objects.exists()
        return context


class AnuncioCreateView(SuccessMessageMixin, CreateView):
    model = Anuncio
    form_class = AnuncioForm
    success_message = 'Anúncio "%(nome)s" criado com sucesso!'
    template_name = 'anuncios/anuncio_create.html'

    def get_success_url(self):
        url = super().get_success_url()
        if 'btn_salvar_e_adicionar_outro' in self.request.POST:
            url = reverse_lazy('anuncios:anuncio_create')
        return url


class AnuncioDetailView(DetailView):
    model = Anuncio
    template_name = 'anuncios/anuncio_detail.html'


class AnuncioUpdateView(SuccessMessageMixin, UpdateView):
    model = Anuncio
    form_class = AnuncioForm
    success_message = 'Anúncio "%(nome)s" alterado com sucesso!'
    template_name = 'anuncios/anuncio_update.html'


class AnuncioDeleteView(SuccessMessageDeletionMixin, DeleteView):
    model = Anuncio
    form_class = AnuncioForm
    success_message = 'Anúncio "%(nome)s" excluído com sucesso!'
    success_url = reverse_lazy('anuncios:anuncio_list')


class AnuncioListView(SingleTableView):
    model = Anuncio
    table_class = AnuncioTable
    template_name = 'anuncios/anuncio_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existem_objetos_cadastrados'] = self.model.objects.exists()
        return context


class AnuncioReportView(FilterView):
    model = Anuncio
    filterset_class = AnuncioFilter
    ordering = ['nome']
    template_name = 'anuncios/anuncio_report.html'

    def get_total_geral(self):
        totais = {
            'investido': 0,
            'visualizacoes': 0,
            'cliques': 0,
            'compartilhamentos': 0,
        }
        for obj in self.object_list:
            totais['investido'] += obj.total_investido
            totais['visualizacoes'] += obj.visualizacoes
            totais['cliques'] += obj.cliques
            totais['compartilhamentos'] += obj.compartilhamentos
        return totais

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_geral'] = self.get_total_geral()
        return context
