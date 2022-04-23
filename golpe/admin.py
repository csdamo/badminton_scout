from django.contrib import admin

from golpe.models import Golpe


class ListandoGolpe(admin.ModelAdmin):
    list_display = ('id', 'descricao_golpe')
    list_display_links = ('id', 'descricao_golpe')
    search_fields = ('descricao_golpe',)
    list_per_page = 10


admin.site.register(Golpe, ListandoGolpe)
