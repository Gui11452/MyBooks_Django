from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login(request):
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method != 'POST':
        return render(request, 'login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario,	password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, 'login.html')

    auth.login(request, user)
    return redirect('inicio')

    

def logout(request):
    auth.logout(request)
    messages.info(request, 'Usuário desconectado!')
    return redirect('login')

"""
@login_required(redirect_field_name='login')
def dashboard(request):
    messages.success(request, 'Você fez o login com sucesso!')
    return redirect('lista')
"""

def registrar(request):
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method != 'POST':
        return render(request, 'registrar.html')

    nome_completo = request.POST.get('nome')
    usuario = request.POST.get('usuario')
    email = request.POST.get('email')
    senha1 = request.POST.get('senha1')
    senha2 = request.POST.get('senha2')

    if not nome_completo or not email or not usuario or not senha1 or not senha2:
        messages.error(request, 'Nenhum campo pode ficar vazio!')
        return render(request, 'registrar.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'E-mail inválido!')
        return render(request, 'registrar.html')

    if len(usuario) < 6:
        messages.error(request, 'O usuário deve ter 6 ou mais caracteres!')
        return render(request, 'registrar.html')

    if senha1 != senha2:
        messages.error(request, 'As senhas tem que ser iguais!')
        return render(request, 'registrar.html')

    if len(senha1) < 6:
        messages.error(request, 'A senha deve ter 6 ou mais caracteres!')
        return render(request, 'registrar.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'O usuário informado já está sendo utilizado!')
        return render(request, 'registrar.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'O E-mail informado já está sendo utilizado!')
        return render(request, 'registrar.html')

    messages.success(request, 'Registrado com sucesso!')
    user = User.objects.create_user(username=usuario, email=email, 
                    password=senha1, first_name=nome_completo)
    user.save()

    return redirect('login')

