from django.contrib import admin

from jogador.models import Jogador


class ListandoJogador(admin.ModelAdmin):
    list_display = ('id', 'nome_jogador', 'data_nascimento', 'lateralidade')
    list_display_links = ('id', 'nome_jogador')
    search_fields = ('nome_jogador',)
    list_editable = ('lateralidade',)
    list_filter = ('lateralidade',)
    list_per_page = 10


admin.site.register(Jogador, ListandoJogador)
