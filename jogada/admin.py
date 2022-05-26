from django.contrib import admin

from jogada.models import Jogada


class ListandoJogada(admin.ModelAdmin):
    list_display = ('id', 'acerto', 'set', 'golpe', 'quadrante')
    list_display_links = ('id', 'acerto')
    list_filter = ('acerto', 'golpe',)
    list_per_page = 10


admin.site.register(Jogada, ListandoJogada)
