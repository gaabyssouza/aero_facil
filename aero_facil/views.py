from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from aero_facil.forms import LoginForm
aeronaves = []

def index(request):
    return render(request, 'index.html')


@require_http_methods(["GET"])
def resultados(request):
    origem = request.GET.get('origem')
    destino = request.GET.get('destino')
    data = request.GET.get('data')
    context = {
        'origem': origem,
        'destino': destino,
        'data': data,
    }
    return render(request, 'resultados.html', context)

@require_http_methods(["GET","POST"])
def login_view(request):
    # Se for GET: mostra página de login
    if request.method == 'GET':
        return render(request, 'login.html')

    # Se for POST: processa login
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    user = authenticate(request, username=email, password=senha)

    if user is not None:
        auth_login(request, user)
        return redirect('painel')

    # Caso inválido
    return render(request, 'login.html', {'login_error': 'Credenciais inválidas'})


def selecionar_assento(request):
    return render(request, 'assento.html')


@login_required
def painel(request):
    global aeronaves

    if request.method == 'POST':
        modelo = request.POST.get('modelo')
        prefixo = request.POST.get('prefixo')

        aeronaves.append({
            'modelo': modelo,
            'prefixo': prefixo,
            'usuario': request.user.username  # salva o dono
        })

        return redirect('painel')

    # Filtra somente as aeronaves do usuário logado
    aeronaves_usuario = [a for a in aeronaves if a['usuario'] == request.user.username]

    return render(request, 'painel.html', {'aeronaves': aeronaves_usuario})

