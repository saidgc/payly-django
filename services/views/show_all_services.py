from django.shortcuts import render
from firebase_db.models.collections import Collections
from firebase_db.models.authentication import FIREBASE_KEY


def show_all_services(request):
    services = Collections().get_all_services()
    is_user_authenticated = None
    if request.user.is_authenticated:
        is_user_authenticated = request.session[FIREBASE_KEY]

    context = {
        'title': "Inicio",
        'services': services,
        'is_user_authenticated': is_user_authenticated
    }
    return render(
        request=request,
        template_name='index.html',
        context=context,
    )
