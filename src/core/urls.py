from django.urls import path

from .views import cadastro, index, v404, v500, carregar_cidades

urlpatterns = [
    path('', index, name='index'),
    path('cadastro', cadastro, name='cadastro'),
    path('404', v404, name='v404'),
    path('500', v500, name='v500'),

    path('ajax/carregar-cidades/', carregar_cidades, name='ajax_carregar_cidades'),
]


