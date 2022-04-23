from django.contrib import admin

from set.models import Set


class ListandoSet(admin.ModelAdmin):
    list_display = ('id', 'partida', 'ordem', 'duracao')
    list_display_links = ('id',)
    list_per_page = 10


admin.site.register(Set, ListandoSet)
