from django.contrib import admin

from tipoerro.models import TipoErro


class ListandoTipoErro(admin.ModelAdmin):
    list_display = ('id', 'descricao_erro')
    list_display_links = ('id', 'descricao_erro')
    search_fields = ('descricao_erro',)
    list_per_page = 10


admin.site.register(TipoErro, ListandoTipoErro)
