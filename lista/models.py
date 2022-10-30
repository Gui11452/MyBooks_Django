from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django import forms 

class Livros(models.Model):
    nome_do_livro = models.CharField(max_length=255, verbose_name="Nome do Livro")

    avaliacao = models.PositiveIntegerField(blank=True, null=True, verbose_name="Avaliação")
    finalizado = models.BooleanField(default=False, verbose_name="Finalizado")
    data_criacao = models.DateTimeField(default=timezone.now)

    resenha = models.TextField(verbose_name="Resenha")
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Usuário")

    foto = models.ImageField(blank=True, null=True, upload_to='fotos/%Y/%m/%d', verbose_name="Foto")

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.nome_do_livro


class FormLivros(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ('nome_do_livro', 'foto', 'avaliacao', 'finalizado', 'resenha')




