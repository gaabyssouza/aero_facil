from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from app.forms import LoginForm

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

@require_http_methods(["POST"])
def login_view(request):
    # Se for GET: mostra página de login
    if request.method == 'GET':
        return render(request, 'accounts/login.html')

    # Se for POST: processa login
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    user = authenticate(request, username=email, password=senha)

    if user is not None:
        auth_login(request, user)
        return redirect('dashboard')

    # Caso inválido
    return render(request, 'accounts/login.html', {'login_error': 'Credenciais inválidas'})

@login_required
def selecionar_assento(request):
    return render(request, 'selecionar_assento.html')

class LoginCustomView(login_view):
    tempate_name = 'accounts/login.html'
    authentication_form = LoginForm
