from django.http import HttpResponseRedirect
from django.shortcuts import render

import firebase_db.models as firebase_authentication
from ..forms.login import LoginForm


def login(request):
    title = 'Inicia sesión'
    login_error = False
    login_form = LoginForm()

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        requested_form = LoginForm(request.POST)
        if requested_form.is_valid():
            email = requested_form.cleaned_data['email']
            password = requested_form.cleaned_data['password']
            if firebase_authentication.login(
                    request=request,
                    user=email,  # TODO change email for user real name
                    email=email,
                    password=password,
            ):
                return HttpResponseRedirect('/')
            else:
                login_error = True

    return render(
        request=request,
        template_name='login.html',
        context={
            'form': login_form,
            'title': title,
            'error': login_error,
        },
    )
