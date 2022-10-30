from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Livros
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import FormLivros

class Counter:
    x = 0

    def incrementar(self):
        self.x+=1
        return ''

    def decrementar(self):
        self.x-=1
        return ''

objeto = Counter()

def lista(request):
    if not request.user.is_authenticated:
        return redirect('inicio')

    livros = Livros.objects.order_by('-data_criacao').filter(usuario=request.user)

    paginator = Paginator(livros, 10)
    page = request.GET.get('p')
    livros = paginator.get_page(page)
    
    if objeto.x == 1:
        objeto.decrementar()

    return render(request, 'lista.html', {
		'livros': livros, 
        'objeto': objeto,
        'numero_de_livros': len(list(livros))
	})

def detalhes(request, livro_id):
    if not request.user.is_authenticated:
        return redirect('inicio')

    livro = get_object_or_404(Livros, id=livro_id)

    usuario = str(livro.usuario)
    
    if request.user.username != usuario:
        return redirect('inicio')

    return render(request, 'detalhes.html', {
        'livro': livro, 
    })

def busca(request):
    if not request.user.is_authenticated:
        return redirect('inicio')

    termo = request.GET.get('termo')
    
    livros = Livros.objects.order_by('-data_criacao').filter(
	    Q(nome_do_livro__icontains=termo), 
        usuario=request.user
    )
    
    paginator = Paginator(livros, 10)
    page = request.GET.get('p')
    livros = paginator.get_page(page)
    
    if objeto.x == 1:
        objeto.decrementar()

    return render(request, 'lista.html', {
		'livros': livros, 
        'objeto': objeto,
        'numero_de_livros': len(list(livros))
	})


def novo_livro(request):
    if not request.user.is_authenticated:
        return redirect('inicio')

    if request.method != 'POST':
        form = FormLivros(request.POST or None, request.FILES or None, instance=Livros(usuario=request.user))
        return render(request, 'novo_livro.html', {'form': form})

    form = FormLivros(request.POST or None, request.FILES or None, instance=Livros(usuario=request.user))

    nome_do_livro = request.POST.get('nome_do_livro')
    avaliacao = request.POST.get('avaliacao')

    avaliacao = 0 if not avaliacao else int(avaliacao)

    if not (avaliacao >= 1 and avaliacao <= 5):
        messages.error(request, 'Escolha uma avaliação entre 1 e 5 estrelas!')
        return render(request, 'novo_livro.html', {'form': form}) 
    
    if not form.is_valid():
        messages.error(request, 'Erro ao enviar o formulário!')
        form = FormLivros(request.POST or None, request.FILES or None, instance=Livros(usuario=request.user))
        return render(request, 'novo_livro.html', {'form': form})

    form.save()
    messages.success(request, f'"{ nome_do_livro }" foi adicionado com sucesso!')
    return render(request, 'novo_livro.html', {'form': form})


def editar_livro(request, livro_id):
    if not request.user.is_authenticated:
        return redirect('inicio')

    livro = get_object_or_404(Livros, id=livro_id)
    if request.method != 'POST':
        form = FormLivros(request.POST or None, request.FILES or None, instance=livro)
        return render(request, 'editar_livro.html', {'form': form, 'livro': livro})

    nome_do_livro = request.POST.get('nome_do_livro')
    avaliacao = request.POST.get('avaliacao')

    form = FormLivros(request.POST or None, request.FILES or None, instance=livro)

    avaliacao = 0 if not avaliacao else int(avaliacao)

    if not (avaliacao >= 1 and avaliacao <= 5):
        messages.error(request, 'Escolha uma avaliação entre 1 e 5 estrelas!')
        return render(request, 'editar_livro.html', {'form': form, 'livro': livro})
    
    if not form.is_valid():
        
        messages.error(request, 'Erro ao enviar o formulário!')
        form = FormLivros(request.POST or None, request.FILES or None, instance=livro)
        return render(request, 'editar_livro.html', {'form': form, 'livro': livro})
    
   
    form.save()
    messages.success(request, 'O livro foi editado com sucesso!')
    return render(request, 'editar_livro.html', {'form': form, 'livro': livro})


def excluir_livro_temporario(request, livro_id):
    if not request.user.is_authenticated:
        return redirect('inicio')

    livro = get_object_or_404(Livros, id=livro_id)
    return render(request, 'excluir_livro.html', {'livro': livro})

def excluir_livro(request, livro_id):
    if not request.user.is_authenticated:
        return redirect('inicio')

    livro = get_object_or_404(Livros, id=livro_id)
    livro.delete()
    return redirect('lista')