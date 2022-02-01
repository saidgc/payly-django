from django.http import HttpResponseRedirect
from django.shortcuts import render

from firebase_db.models.authentication import FIREBASE_KEY


def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    is_user_authenticated = request.session[FIREBASE_KEY]
    context = {
        'title': 'Cuenta',
        'is_user_authenticated': is_user_authenticated,
        'admin': False,
    }
    return render(
        request=request,
        template_name='account.html',
        context=context,
    )
