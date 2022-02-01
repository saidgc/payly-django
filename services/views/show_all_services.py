from django.shortcuts import render
from firebase_db.models.collections import Collections
from firebase_db.models.authentication import FIREBASE_KEY


def show_all_services(request):
    services = Collections().get_all_services()

    context = {
        'title': "Inicio",
        'services': services,
    }
    return render(
        request=request,
        template_name='index.html',
        context=context,
    )
