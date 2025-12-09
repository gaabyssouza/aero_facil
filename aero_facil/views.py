from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login

from .models import Aircraft  # Import do modelo Aircraft


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


@require_http_methods(["GET", "POST"])
def login_view(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            usuario = form.get_user()
            auth_login(request, usuario)
            return redirect("painel")

    return render(request, "login.html", {"form": form})


def selecionar_assento(request):
    return render(request, 'assento.html')


@login_required
def painel(request):
    if request.method == "POST":
        model_name = request.POST.get("modelo")
        prefixo = request.POST.get("prefixo")

        # Cria nova aeronave do usuário logado
        Aircraft.objects.create(
            owner=request.user,
            model_name=model_name,
            prefixo=prefixo,
            capacity=4  # valor padrão
        )

        return redirect("painel")

    # Busca aeronaves do usuário logado
    aeronaves_usuario = Aircraft.objects.filter(owner=request.user)

    return render(request, "painel.html", {"aeronaves": aeronaves_usuario})
