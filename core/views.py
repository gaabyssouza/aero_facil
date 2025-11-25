from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Página inicial (index)
def index_view(request):
    """
    Renderiza a home (index.html). Se ?login_error=1 na querystring abrirá o modal com erro.
    """
    login_error = request.GET.get("login_error") == "1"
    return render(request, "index.html", {"login_error": login_error})


# Login (recebe POST do modal)
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "index.html", {"login_error": True})

    return redirect("index")


# Logout
def logout_view(request):
    logout(request)
    return redirect("index")


# Dashboard (requer login)
@login_required
def dashboard_view(request):
    return render(request, "dashboard.html", {})


# ➕ NOVA VIEW — Registrar usuário
def registrar(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("password")

        # Verifica duplicações
        if User.objects.filter(username=username).exists():
            messages.error(request, "Este usuário já existe.")
            return redirect("registrar")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está em uso.")
            return redirect("registrar")

        # Criar usuário
        User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )

        messages.success(request, "Conta criada com sucesso! Faça login.")
        return redirect("index")

    return render(request, "registrar.html")
