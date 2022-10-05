from django.contrib import admin
from .models import Livros

# .models = arquivo python models na mesma pasta

class LivrosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_do_livro', 'avaliacao', 'finalizado', 'data_criacao', 'usuario')
    list_display_links = ('id', 'nome_do_livro', 'nome_do_livro')
    list_filter = ('nome_do_livro', 'finalizado', 'usuario')
    list_per_page = 10	
    search_fields = ('nome_do_livro', 'usuario')
"""
class UsuariosAdmin(admin.ModelAdmin):
    list_filter = ('nome',)
    search_fields = ('nome',)

admin.site.register(Usuario, UsuariosAdmin)"""
admin.site.register(Livros, LivrosAdmin)
