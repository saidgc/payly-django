import requests
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from ..forms.login import LoginForm
from ..helpers.firebase_auth import auth as firebase


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
            try:
                firebase_user = firebase.sign_in_with_email_and_password(
                    email,
                    password,
                )
            except requests.exceptions.HTTPError:
                login_error = True
            else:
                django_user = auth.authenticate(
                    request,
                    username=firebase_user['email'],
                    password=password,
                )
                if not django_user:
                    django_user = User.objects.create_user(
                        firebase_user['email'],  # TODO change email for user real name
                        firebase_user['email'],
                        password,
                    )
                auth.login(request, django_user)
                return HttpResponseRedirect('/')

    return render(
        request=request,
        template_name='login.html',
        context={
            'form': login_form,
            'title': title,
            'error': login_error,
        },
    )
