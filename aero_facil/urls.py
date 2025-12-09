from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('', views.index, name='index'),
    path('resultados/', views.resultados, name='resultados'),
    path('login/', views.login_view, name='login'),
    path('selecionar_assento/', views.selecionar_assento, name='selecionar_assento'),
    path('painel/', views.painel, name='painel'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

