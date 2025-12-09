from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Aeronave

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Usuário'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Senha'
    }))

class AeronaveForm(forms.ModelForm):
    class Meta:
        model = Aeronave
        fields = ['modelo', 'prefixo', 'status']

        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modelo'}),
            'prefixo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prefixo'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }