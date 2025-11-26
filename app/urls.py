from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resultados', views.resultados, name='resultados'),
    path('login', views.login_view, name='login'),
    path('selecionar_assento/', views.selecionar_assento, name='selecionar_assento'),
]
