from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resultados/', views.resultados, name='resultados'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('selecionar_assento/', views.selecionar_assento, name='selecionar_assento'),
]
