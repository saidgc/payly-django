from django.http import HttpResponseRedirect
from django.shortcuts import render


def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    context = {
        'title': 'Cuenta',
    }
    return render(
        request=request,
        template_name='account.html',
        context=context,
    )
