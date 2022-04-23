from django.contrib import admin

from quadrante.models import Quadrante


class ListandoQuadrane(admin.ModelAdmin):
    list_display = ('id', 'descricao_quadrante', 'lado',)
    list_display_links = ('id', 'descricao_quadrante')
    search_fields = ('descricao_quadrante',)
    list_per_page = 10


admin.site.register(Quadrante, ListandoQuadrane)
