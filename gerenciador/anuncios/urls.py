from django.urls import path

from .views import (
    AnuncioCreateView,
    AnuncioDetailView,
    AnuncioUpdateView,
    AnuncioDeleteView,
    AnuncioListView,
    ClienteCreateView,
    ClienteDetailView,
    ClienteUpdateView,
    ClienteDeleteView,
    ClienteListView,
)

app_name = 'anuncios'

urlpatterns = [
    path('', AnuncioListView.as_view(), name='anuncio_list'),
    path('novo/', AnuncioCreateView.as_view(), name='anuncio_create'),
    path('<uuid:pk>/detalhar/', AnuncioDetailView.as_view(), name='anuncio_detail'),
    path('<uuid:pk>/editar/', AnuncioUpdateView.as_view(), name='anuncio_update'),
    path('<uuid:pk>/excluir/', AnuncioDeleteView.as_view(), name='anuncio_delete'),
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/novo/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<uuid:pk>/detalhar/', ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/<uuid:pk>/editar/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<uuid:pk>/excluir/', ClienteDeleteView.as_view(), name='cliente_delete'),
]
