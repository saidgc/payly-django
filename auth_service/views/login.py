from django.http import HttpResponseRedirect
from django.shortcuts import render

from auth_service.forms.login import LoginForm
from firebase_db.models.authentication import FirebaseAuthentication

TITLE = 'Inicia sesión'

login_form = LoginForm()


def login_view(request):
    login_error = False

    if request.user.is_authenticated:
        return HttpResponseRedirect('/services')

    if request.method == 'POST':
        requested_form = LoginForm(request.POST)
        if requested_form.is_valid():
            email = requested_form.cleaned_data['email']
            password = requested_form.cleaned_data['password']
            login_result = FirebaseAuthentication().login(
                request=request,
                user=email,  # TODO change email for user real name
                email=email,
                password=password,
            )
            if login_result:
                return HttpResponseRedirect('/services')
            else:
                login_error = True

    context = {
        'form': login_form,
        'title': TITLE,
        'error': login_error,
    }
    return render(
        request=request,
        template_name='login.html',
        context=context,
    )
