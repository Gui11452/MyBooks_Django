from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django import forms 

class Livros(models.Model):
    nome_do_livro = models.CharField(max_length=255)

    avaliacao = models.PositiveIntegerField(blank=True, null=True)
    finalizado = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=timezone.now)

    resenha = models.TextField()
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    foto = models.ImageField(blank=True, null=True, upload_to='fotos/%Y/%m/%d')

    def __str__(self):
        return self.nome_do_livro


class FormLivros(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ('nome_do_livro', 'foto', 'avaliacao', 'finalizado', 'resenha')




