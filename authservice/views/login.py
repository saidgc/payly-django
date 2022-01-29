from django.shortcuts import render
from ..forms.login import LoginForm


def login(request):
    form = LoginForm()
    return render(request, 'login.html', context={'form': form, 'title': 'Inicia sesión'})
