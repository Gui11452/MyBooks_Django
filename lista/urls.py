from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name="lista"),
    path('busca/', views.busca, name="busca"),
    path('<int:livro_id>', views.detalhes, name="detalhes"),
    path('novo_livro/', views.novo_livro, name='novo_livro'),
    path('editar/<int:livro_id>', views.editar_livro, name="editar_livro"),
    path('excluir/<int:livro_id>', views.excluir_livro_temporario, name="excluir_livro_temporario"),
    path('excluir_definitivo/<int:livro_id>', views.excluir_livro, name="excluir_livro"),
]