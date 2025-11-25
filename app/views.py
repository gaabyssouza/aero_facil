from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

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
    # se seu username não for email, ajuste abaixo
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    user = authenticate(request, username=email, password=senha)
    if user is not None:
        auth_login(request, user)
        return redirect('dashboard')
    # fallback: retornar index com erro
    return render(request, 'index.html', {'login_error': 'Credenciais inválidas'})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
