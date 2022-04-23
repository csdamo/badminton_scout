from django.contrib import admin

from jogada.models import Jogada


class ListandoJogada(admin.ModelAdmin):
    list_display = ('id', 'status', 'set', 'jogador', 'golpe', 'quadrante')
    list_display_links = ('id', 'status')
    list_filter = ('status', 'jogador', 'golpe',)
    search_fields = ('status', 'jogador')
    list_per_page = 10


admin.site.register(Jogada, ListandoJogada)
