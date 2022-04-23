from django.contrib import admin

from partida.models import Partida


class ListandoPartida(admin.ModelAdmin):
    list_display = (
        'id', 'tipo_jogo', 'data_partida', 'jogador_1', 'jogador_2',
        'jogador_adversario_1', 'jogador_adversario_2')
    list_display_links = ('id', 'tipo_jogo')
    search_fields = (
        'tipo_partida', 'jogador_1', 'jogador_2', 'jogador_adversario_1', 'jogador_adversario_2')
    list_filter = ('tipo_jogo',)
    list_per_page = 10


admin.site.register(Partida, ListandoPartida)